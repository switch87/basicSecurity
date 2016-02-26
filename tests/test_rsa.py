import pytest

from CryptoController.Rsa import RsaController


@pytest.fixture
def rsacs():  # RSA Controller Server
    return RsaController("m", bits=512)


@pytest.fixture
def rsacc(rsacs):  # RSA Controller Client
    return RsaController("c", bits=512, pubkey=rsacs.pubkey)


def test_program_generates_private_and_public_rsa_and_saves_to_files(rsacs):
    rsacs.save_keys('Public_A', 'Private_A')

    assert RsaController.load_private_key('Private_A')
    assert RsaController.load_public_key('Public_A')


def test_rsa_server_and_client_have_same_public_key(rsacs, rsacc):
    assert rsacs.pubkey == rsacc.pubkey


def test_rsa_client_must_have_public_key():
    with pytest.raises(NotImplementedError):
        RsaController("c")


def test_string_can_be_validated_with_md5_signature(rsacs):
    string = "Hallo allemaal!"

    encrypted = rsacs.encrypt(string)
    signature = rsacs.sign_with_md5(string)

    decrypted = rsacs.decrypt(encrypted)
    assert rsacs.verify_signature(decrypted, signature)


def test_controller_can_be_generated_with_key_files(rsacs):
    rsacs.save_keys('Public_A', 'Private_A')

    rsacc = RsaController("c", bits=512, pubfile='Public_A')
    rsacs2 = RsaController("m", bits=512, privfile='Private_A')

    assert rsacs.pubkey == rsacc.pubkey
    assert rsacs.privkey == rsacs2.privkey


def test_controller_type_must_be_defined():
    with pytest.raises(TypeError):
        RsaController("d", bits=512)
