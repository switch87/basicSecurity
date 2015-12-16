import rsa


class RsaController():

    def __init__(self, type, privkey=None, pubkey=None, bits=1024, privfile=None, pubfile=None):
        self.bits = bits

        if pubfile:
            pubkey = self.load_public_key(pubfile)
        if privfile:
            privkey = self.load_private_key(privfile)

        if type == "m":
            if privkey is None:
                (self.pubkey, self.privkey) = self.generate_rsa(self.bits)
            else:
                (self.pubkey, self.privkey) = (pubkey, privkey)

        elif type == "c":
            if pubkey is None:
                raise NotImplementedError
            self.pubkey = pubkey

        else:
            raise TypeError

    def save_keys(self, file_public, file_private=None):
        if self.privkey is not None:
            open(file_private, 'w').write(self.privkey._save_pkcs1_pem())
        open(file_public, 'w').write(self.pubkey._save_pkcs1_pem())

    @classmethod
    def load_private_key(cls, file_private):
        with open(file_private) as file:
            return rsa.PrivateKey.load_pkcs1(file.read())

    @classmethod
    def load_public_key(cls, file_public):
        with open('Public_A') as file:
            return rsa.PublicKey.load_pkcs1(file.read())

    @classmethod
    def generate_rsa(cls, bits):
        return rsa.newkeys(bits, poolsize=8)

    def encrypt_public(self, string):
        return rsa.encrypt(string, self.pubkey)

    def decrypt_private(self, string):
        return rsa.decrypt(string, self.privkey)

    def encrypt_private(self, string):
        return rsa.encrypt(string, self.privkey)

    def decrypt_public(self, string):
        return self.pubkey.decrypt(string)

    def sign_with_md5(self, message):
        return rsa.sign(message, self.privkey, "MD5")

    def verify_signature(self, message, signature):
        return rsa.verify(message, signature, self.pubkey)
