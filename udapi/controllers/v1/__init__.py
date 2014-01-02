from pecan import expose
from udapi.controllers.v1.host import HostController
from udapi.controllers.v1.cert import CertController
from udapi.controllers.v1.autocert import AutoCertController


class V1Controller(object):

    def __init__(self):
        super(V1Controller, self).__init__()
        self.hosts = HostController()
        self.certs = CertController()
        self.autoca = AutoCertController()

    @expose('json')
    def index(self):
        return sorted(self.__dict__.keys())

