from pecan import expose, abort, conf
from pecan.rest import RestController
import time
from webob.exc import status_map

class BaseIndexController(object):
    @expose('json')
    def index(self):
        return self.__dict__.keys()

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)


class BaseRestController(RestController):

    _custom_actions = {
        'expand': ['GET']
    }

    def __init__(self):
        self.stuff = {}
        self.update = 0
        self.error = False

    def _check_refresh(self):
        if self.update < (time.time() - conf.cache_time):
            try:
                self._refresh()
                self.error = False
            except:
                self.error = True

    def _refresh(self):
        pass

    @expose('json')
    def expand(self):
        self._check_refresh()
        data = []
        for k in sorted(self.stuff.keys()):
            data.append(self.stuff[k].to_data())

        return {'update': time.strftime('%c', time.localtime(self.update)),
                'message': data,
                'error': self.error,
        }

    @expose('json')
    def get_all(self):
        self._check_refresh()
        return {'update': time.strftime('%c', time.localtime(self.update)),
                'message': sorted(self.stuff.keys()),
                'error': self.error,
        }

    @expose('json')
    def get_one(self, thing):
        self._check_refresh()
        if thing in self.stuff.keys():
            return {'update': time.strftime('%c', time.localtime(self.update)),
                    'message': self.stuff[thing].to_data(),
                    'error': self.error,
            }
        abort(404)
