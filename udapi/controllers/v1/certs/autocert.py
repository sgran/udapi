from pecan import conf

from udapi.controllers.v1.certs.cert import CertController


class AutoCertController(CertController):
    def __init__(self):
        super(AutoCertController, self).__init__()
        self.root_dir = conf.auto_cert_dir
