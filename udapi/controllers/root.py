from pecan import expose

from udapi.controllers.base import BaseIndexController
from udapi.controllers.v1 import V1Controller


class RootController(BaseIndexController):

    def __init__(self):
        super(RootController, self).__init__()
        self.v1 = V1Controller()
