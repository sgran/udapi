from pecan import expose
from webob.exc import status_map

from udapi.controllers.v1 import V1Controller


class RootController(object):

    def __init__(self):
        super(RootController, self).__init__()
        self.v1 = V1Controller()

    @expose('json')
    def index(self):
        return {'versions': self.__dict__.keys()}

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
