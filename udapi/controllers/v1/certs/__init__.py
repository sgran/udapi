from pecan import expose
from udapi.controllers.v1.certs.autocert import AutoCertController
from udapi.controllers.v1.certs.external import ExternalCertController


class CertsController(object):

    def __init__(self):
        super(CertsController, self).__init__()
        self.autoca = AutoCertController()
        self.external = ExternalCertController()

    @expose('json')
    def index(self):
        return sorted(self.__dict__.keys())

