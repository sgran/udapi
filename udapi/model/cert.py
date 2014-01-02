import copy
import OpenSSL
import time

class SSLCert(object):

    def __init__(self, name):
        self.subject = {}
        self.issuer = {}
        self.body = None
        self.notafter = None
        self.notbefore = None

        with open(name) as f:
            cert = f.read()
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            for k, v in x509.get_subject().get_components():
                self.subject[k] = v
            for k, v in x509.get_issuer().get_components():
                self.issuer[k] = v

            self.body = cert
            self.notafter = time.strptime(x509.get_notAfter(), '%Y%m%d%H%M%SZ')
            self.notbefore = time.strptime(x509.get_notBefore(), '%Y%m%d%H%M%SZ')

    def to_data(self):
        data = copy.deepcopy(self.__dict__)
        data['notbefore'] = time.strftime('%c', data['notbefore'])
        data['notafter'] = time.strftime('%c', data['notafter'])
        return data
