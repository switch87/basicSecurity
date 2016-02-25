import base64
import os
from Crypto.Cipher import AES


class AesController():
    BLOCK_SIZE = 32
    PADDING = '{'

    def __init__(self, cipher=None, **kwargs):
        """
        Initialize new AES Controller.
        If cipher is not given, generate a random cipher, else save given cipher.

        :param cipher: cipher
        :param kwargs:
        :return: None
        """

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
    def encrypt(self, s):
        return base64.b64encode(self.cipher.encrypt(self.pad(s)))

    def encrypt_file(self, infile, outfile):
        finished = False
        while not finished:
            chunk = infile.read(1024 * self.BLOCK_SIZE)
            if len(chunk) == 0 or len(chunk) % self.BLOCK_SIZE != 0:
                padding_length = self.BLOCK_SIZE - (len(chunk) % self.BLOCK_SIZE)
                chunk += padding_length * chr(padding_length)
                finished = True
            outfile.write(self.cipher.encrypt(chunk))

    def decrypt(self, e):
        """
        Decrypt AES encrypted string
        :param e: string
        :return: string
        """

        return self.cipher.decrypt(base64.b64decode(e)).rstrip(self.PADDING)

    def decrypt_file(self, infile, outfile):
        next_chunk = ''
        finished = False
        while not finished:
            chunk, next_chunk = next_chunk, self.cipher.decrypt(infile.read(1024 * self.BLOCK_SIZE))
            if len(next_chunk) == 0:
                padding_length = ord(chunk[-1])
                chunk = chunk[:-padding_length]
                finished = True
            outfile.write(chunk)

    @classmethod
    def generate_random_cipher(cls, **kwargs):
        """
        Generate a random secret key
        :param kwargs:
        :return: cipher
        """

        cls.secret = os.urandom(cls.BLOCK_SIZE)
        return AES.new(cls.secret)
