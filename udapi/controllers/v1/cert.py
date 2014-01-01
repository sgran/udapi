import os
from pecan.rest import RestController
from pecan import expose, abort, conf
import time

from udapi.model.cert import SSLCert


class CertController(RestController):
    def __init__(self):
        self.certs = {}
        self.update = 0
        self.root_dir = conf.cert_dir

    def _check_refresh(self):
        if self.update < (time.time() - conf.cache_time):
            self._refresh()

    def _refresh(self):
        for f in os.listdir(self.root_dir):
            if not f.endswith('.crt'):
                continue
            short = f[:-4]
            self.certs[short] = SSLCert(os.path.join(self.root_dir, f))
        self.update = time.time()

    @expose('json')
    def get_all(self):
        self._check_refresh()
        return {'update': self.update,
                'message': sorted(self.certs.keys()),
        }

    @expose('json')
    def get_one(self, cert):
        self._check_refresh()
        if cert in self.certs.keys():
            return {'update': self.update,
                    'message': self.certs[cert].to_data()
            }
        abort(404)

