import base64
import os
from Crypto.Cipher import AES


class AesController():
    BLOCK_SIZE = 32
    PADDING = '{'

    def __init__(self, cipher=None, **kwargs):
        if cipher is None:
            self.cipher = self.generate_random_cipher()
        elif isinstance(cipher, str):
            self.cipher = AES.new(cipher)
        else:
            self.cipher = cipher

    # one-liner to sufficiently pad the text to be encrypted
    def pad(self, s, **kwargs):
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING

    # one-liners to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    def encode_aes(self, s):
        if self.cipher is None:
            self.generate_random_cipher()
        return base64.b64encode(self.cipher.encrypt(self.pad(s)))

    def decode_aes(self, e):
        return self.cipher.decrypt(base64.b64decode(e)).rstrip(self.PADDING)

    # generate a random secret key
    @classmethod
    def generate_random_cipher(cls, **kwargs):
        cls.secret = os.urandom(cls.BLOCK_SIZE)
        return AES.new(cls.secret)
