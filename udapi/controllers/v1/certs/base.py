import os
from pecan import conf
import time

from udapi.controllers.base import BaseRestController
from udapi.model.cert import SSLCert


class CertController(BaseRestController):
    def __init__(self):
        super(CertController, self).__init__()
        self.root_dir = conf.cert_dir

    def _refresh(self):
        for f in os.listdir(self.root_dir):
            if not f.endswith('.crt'):
                continue
            short = f[:-4]
            self.stuff[short] = SSLCert(os.path.join(self.root_dir, f))
        self.update = time.time()
