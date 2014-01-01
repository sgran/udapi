import os
from pecan.rest import RestController
from pecan import expose, abort
import time

from udapi.model.cert import SSLCert


class CertController(RestController):
    certs = {}
    update = 0

    def _check_refresh(self):
        if self.update < (time.time() - 60):
            self._refresh()

    def _refresh(self):
        root_dir = '/home/steve/source/git/dsa/dsa-puppet/modules/ssl/files/servicecerts'
        for f in os.listdir(root_dir):
            short = f[:-4]
            self.certs[short] = SSLCert(os.path.join(root_dir, f))
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

