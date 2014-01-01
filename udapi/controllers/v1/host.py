import ldap
from pecan.rest import RestController
from pecan import expose, abort, conf
import time

from udapi.model.host import Host


class HostController(RestController):

    def __init__(self):
        self.hosts = {}
        self.update = 0
        self._refresh()

    def _check_refresh(self):
        if self.update < (time.time() - conf.cache_time):
            self._refresh()

    def _refresh(self):
        l = ldap.initialize('ldap://db.debian.org')
        r = l.search_s('dc=debian,dc=org',ldap.SCOPE_SUBTREE,'(hostname=*.debian.org)')
        for dn,entry in r:
            self.hosts[entry['host'][0]] = (Host(entry))
        l.unbind_ext_s()
        self.update = time.time()

    @expose('json')
    def get_all(self):
        self._check_refresh()
        return {'update': self.update,
                'message': sorted(self.hosts.keys()),
        }

    @expose('json')
    def get_one(self, hostname):
        self._check_refresh()
        if hostname in self.hosts.keys():
            return {'update': self.update,
                    'message': self.hosts[hostname].to_data()
            }
        abort(404)
