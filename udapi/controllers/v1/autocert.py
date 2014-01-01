import os
from pecan import expose, abort, conf
import time

from udapi.controllers.v1.cert import CertController


class AutoCertController(CertController):
    def __init__(self):
        self.certs = {}
        self.update = 0
        self.root_dir = conf.auto_cert_dir
