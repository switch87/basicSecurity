from Crypto.Cipher import AES

import pytest

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
    encoded = aesc.encode_aes("Hallo")
    assert encoded != "Hallo"


def test_decoding_gives_original_text(aesc):
    text = "Oef, ik ben intact"
    encoded = aesc.encode_aes(text)
    assert aesc.decode_aes(encoded) == text


def test_aes_controller_can_be_passed_an_existing_sipher(aesc):
    aesc2 = AesController(cipher=aesc.cipher)

    text = "Ik ben identiek na Encoding!"
    assert aesc.encode_aes(text) == aesc2.encode_aes(text)


def test_two_aes_controllers_are_not_the_same(aesc):
    aesc2 = AesController()

    text = "Ik ben uniek!"
    assert aesc.encode_aes(text) != aesc2.encode_aes(text)
