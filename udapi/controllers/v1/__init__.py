from pecan import expose

from udapi.controllers.base import BaseIndexController
from udapi.controllers.v1.host import HostController
from udapi.controllers.v1.certs import CertsController
from udapi.controllers.v1.domain import DomainController


class V1Controller(BaseIndexController):

    def __init__(self):
        super(V1Controller, self).__init__()
        self.hosts = HostController()
        self.certs = CertsController()
        self.domains = DomainController()
