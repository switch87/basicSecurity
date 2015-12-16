import os
import urllib
from Crypto.Cipher import AES

import pytest
import filecmp

from CryptoController.Aes import AesController


@pytest.fixture
def aesc():
    aesc = AesController()
    return aesc


def test_program_generates_an_aes_key(aesc):
    assert isinstance(aesc.cipher, AES.AESCipher)


def test_strings_get_padded_to_encryptable_length(aesc):
    assert len(aesc.pad("Hallo")) == 32
    assert aesc.pad("Alles goed?").endswith("{")
    assert len(aesc.pad("Ik ben al wat langer maar nog niet lang genoeg", BLOCK_SIZE=64)) == 64


def test_string_can_be_encrypted(aesc):
    encoded = aesc.encrypt("Hallo")
    assert encoded != "Hallo"


def test_decoding_gives_original_text(aesc):
    text = "Oef, ik ben intact"
    encoded = aesc.encrypt(text)
    assert aesc.decrypt(encoded) == text


def test_aes_controller_can_be_passed_an_existing_sipher(aesc):
    aesc2 = AesController(cipher=aesc.cipher)

    text = "Ik ben identiek na Encoding!"
    assert aesc.encrypt(text) == aesc2.encrypt(text)


def test_two_aes_controllers_are_not_the_same(aesc):
    aesc2 = AesController()

    text = "Ik ben uniek!"
    assert aesc.encrypt(text) != aesc2.encrypt(text)


def test_make_aes_controller_with_given_cipher_as_string(aesc):
    cipher = aesc.secret
    aesc2 = AesController(cipher)

    text = "Ik ben identiek na Encoding!"
    assert aesc.encrypt(text) == aesc2.encrypt(text)


# File encryption
def test_a_file_can_be_encrypted(aesc):
    original = "original.jpeg"
    encrypted = "decryptMe.jpeg"
    decrypted = "amITheSame.jpeg"

    if not os.path.isfile(original):
        urllib.urlretrieve(
            "http://www.themarysue.com/wp-content/uploads/2010/11/periodic-table-final-fantasy-characters.jpeg",
            original
        )

    for file in [encrypted, decrypted]:
        if os.path.isfile(file):
            os.remove(file)

    with open(original, 'rb') as infile, open(encrypted, 'wb') as outfile:
        aesc.encrypt_file(infile, outfile)
    with open(encrypted, 'rb') as infile, open(decrypted, 'wb') as outfile:
        aesc.decrypt_file(infile, outfile)
    assert filecmp.cmp(original, decrypted)

    for file in [encrypted, decrypted]:
        os.remove(file)
