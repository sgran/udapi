import copy
import ldap
from pecan import conf, expose
import time

from udapi.controllers.base import BaseRestController
from udapi.model.dns import RRSet


class DebNetController(BaseRestController):

    def _refresh(self):
        l = ldap.initialize('ldap://db.debian.org')
        r = l.search_s('dc=debian,dc=org',
            ldap.SCOPE_SUBTREE,
            '(dnsZoneEntry=*)',
            ['dnsZoneEntry'])

        entries = {}
        for dn,record in r:
            data = record['dnsZoneEntry']
            for entry in data:
                atoms = entry.split()
                name = atoms[0]
                if not entries.get(name):
                    entries[name] = []
                entries[name].append(entry)

        records = {}
        for name, data in entries.iteritems():
            records[name] = RRSet(name, data)
        l.unbind_ext_s()

        self.stuff = copy.deepcopy(records)
        self.update = time.time()


class DomainController(BaseRestController):

    def __init__(self):
        super(DomainController, self).__init__()
        self.__dict__['debian.net'] = DebNetController()

    @expose('json')
    def index(self):
        data = copy.deepcopy(self.__dict__.keys())
        data.remove('stuff')
        data.remove('update')
        return sorted(data)
