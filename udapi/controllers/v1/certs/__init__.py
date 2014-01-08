from pecan import expose

from udapi.controllers.base import BaseIndexController
from udapi.controllers.v1.certs.autocert import AutoCertController
from udapi.controllers.v1.certs.external import ExternalCertController


class CertsController(BaseIndexController):

    def __init__(self):
        super(CertsController, self).__init__()
        self.autoca = AutoCertController()
        self.external = ExternalCertController()
