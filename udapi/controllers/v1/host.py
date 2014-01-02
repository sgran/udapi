import ldap
from pecan import conf
import time

from udapi.model.host import Host
from udapi.controllers.base import BaseRestController


class HostController(BaseRestController):

    def _refresh(self):
        l = ldap.initialize('ldap://db.debian.org')
        r = l.search_s('dc=debian,dc=org',ldap.SCOPE_SUBTREE,'(hostname=*.debian.org)')
        for dn,entry in r:
            self.stuff[entry['host'][0]] = (Host(entry))
        l.unbind_ext_s()
        self.update = time.time()
