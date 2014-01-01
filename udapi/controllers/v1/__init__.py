from pecan import expose
from udapi.controllers.v1.host import HostController
from udapi.controllers.v1.cert import CertController


class V1Controller(object):
    @expose('json')
    def index(self):
        return ['certs', 'hosts']

    hosts = HostController()
    certs = CertController()
