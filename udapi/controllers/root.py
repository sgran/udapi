from pecan import expose
from webob.exc import status_map

import udapi.controllers.v1


class RootController(object):

    @expose('json')
    def index(self):
        return {'versions': ['v1']}

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
    v1 = udapi.controllers.v1.V1Controller()
