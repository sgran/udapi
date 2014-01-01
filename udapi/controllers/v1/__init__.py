from pecan import expose
from udapi.controllers.v1.host import HostController
from udapi.controllers.v1.cert import CertController
from udapi.controllers.v1.autocert import AutoCertController


class V1Controller(object):
    @expose('json')
    def index(self):
        return ['autoca', 'certs', 'hosts']

    hosts = HostController()
    certs = CertController()
    autoca = AutoCertController()
