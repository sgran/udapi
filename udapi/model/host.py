class Host(object):

    flattened_keys = [
        'access',
        'admin',
        'architecture',
        'bandwidth',
        'disk',
        'distribution',
        'dnsTTL',
        'host',
        'hostname',
        'machine',
        'memory',
        'mXRecord',
        'physicalHost',
        'sponsor-admin',
        'sshRSAHostKey',
        'status',
    ]
    strip_keys = [
        'objectClass'
    ]

    def __init__(self, entry):
        for k, v in entry.iteritems():
            if k in self.flattened_keys:
                if len(v) != 1:
                    raise RuntimeError("len(%s) != 1: %s" % (k, v))
                self.__dict__[k] = v[0]
            elif k in self.strip_keys:
                continue
            else:
                self.__dict__[k] = v

    def to_data(self):
        return self.__dict__
