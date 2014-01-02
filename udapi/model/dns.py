class RRSet(object):

    def __init__(self, name, data):

        self.name = name
        self.rrs = {}

        for entry in data:
            # foo IN CNAME bar
            atoms = entry.split()
            rrtype = atoms[2].lower()
            if self.rrs.get(rrtype):
                if rrtype == 'cname':
                    raise RuntimeError("CNAME record already present for %s" % name)
            else:
                self.rrs[rrtype] = []
            self.rrs[rrtype].append(' '.join(atoms[3:]))

    def to_data(self):
        return self.rrs
