import gtk
import pygtk

from CryptoController.Aes import AesController
from CryptoController.Rsa import RsaController

pygtk.require('2.0')


class EncryptionWindow:
    # Files to save to
    pub_a = "Public_A"
    pub_b = "Public_B"
    priv_a = "Private_A"
    priv_b = "Private_B"
    file_1 = "File_1"
    file_2 = "File_2"
    file_3 = "File_3"

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.generate_keys()
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("AvocadoCrypto - encrypt")
        self.window.set_icon_from_file('icon.png')
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)

        self.box1 = gtk.VBox(False, 0)
        self.window.add(self.box1)

        self.label1 = gtk.Label("Alice Public: \n" +
                                self.rsa_controller1.pubkey._save_pkcs1_pem() + "\n")
        self.box1.pack_start(self.label1, True, True, 0)
        self.label1.show()

        self.label2 = gtk.Label("Bob Public: \n" +
                                self.rsa_controller2.pubkey._save_pkcs1_pem() + "\n")
        self.box1.pack_start(self.label2, True, True, 0)
        self.label2.show()

        self.input_to_encrypt = gtk.Entry(max=0)
        self.box1.pack_start(self.input_to_encrypt, True, True, 0)
        self.input_to_encrypt.show()

        self.button1 = gtk.Button("Encrypt the text")
        self.box1.pack_start(self.button1, True, True, 0)
        self.button1.connect("clicked", self.encrypt)
        self.button1.show()

        self.box1.show()
        self.window.show()

    def generate_keys(self):
        self.aes_controller = AesController()
        self.rsa_controller1 = RsaController('m')
        self.rsa_controller1.save_keys(self.pub_a, self.priv_a)
        self.rsa_controller2 = RsaController('m')
        self.rsa_controller2.save_keys(self.pub_b, self.priv_b)

    def main(self):
        gtk.main()

    def encrypt(self, widget):
        self.label1.set_text(self.aes_controller.encode_aes(self.input_to_encrypt.get_text()))

        # Programma gebruikt de symmetric key om de boodschap te encrypteren,
        # en saved het resultaat in een file (File_1)
        open(self.file_1, 'w').write(self.aes_controller.encode_aes(self.input_to_encrypt.get_text()))

        # Programma encrypteert de symmetric key met de public key van Bob,
        # en saved het resultaat in een file (File_2)
        open(self.file_2, 'w').write(self.rsa_controller2.encrypt_public(self.aes_controller.secret))

        # Programma maakt een hash van de oorspronkelijke boodschap
        # Programma encrypteert die hash met de private key van Alice,
        # en saved het resultaat in een file (File_3)
        open(self.file_3, 'w').write(self.rsa_controller1.sign_with_md5(self.input_to_encrypt.get_text()))
