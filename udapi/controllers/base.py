from pecan import expose, abort, conf
from pecan.rest import RestController
import time


class BaseRestController(RestController):
    def __init__(self):
        self.stuff = {}
        self.update = 0

    def _check_refresh(self):
        if self.update < (time.time() - conf.cache_time):
            self._refresh()

    def _refresh(self):
        pass

    @expose('json')
    def get_all(self):
        self._check_refresh()
        return {'update': time.strftime('%c', time.localtime(self.update)),
                'message': sorted(self.stuff.keys()),
        }

    @expose('json')
    def get_one(self, thing):
        self._check_refresh()
        if thing in self.stuff.keys():
            return {'update': time.strftime('%c', time.localtime(self.update)),
                    'message': self.stuff[thing].to_data()
            }
        abort(404)
