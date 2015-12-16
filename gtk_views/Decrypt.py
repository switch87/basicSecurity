import gtk
import pygtk

from CryptoController.Aes import AesController
from CryptoController.Rsa import RsaController

pygtk.require('2.0')


class DecryptionWindow:
    # Files to save to
    pub_a = "Public_A"
    priv_b = "Private_B"
    file_1 = "File_1"
    file_2 = "File_2"
    file_3 = "File_3"

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.get_keys()
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("AvocadoCrypto - Decrypt")
        self.window.set_icon_from_file('icon.png')
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)

        self.box1 = gtk.VBox(False, 0)
        self.window.add(self.box1)

        if self.ok:
            self.label1 = gtk.Label("YES!\n")
        else:
            self.label1 = gtk.Label("NO!\n")
        self.box1.pack_start(self.label1, True, True, 0)
        self.label1.show()

        self.label2 = gtk.Label(self.text)
        self.box1.pack_start(self.label2, True, True, 0)
        self.label2.show()

        self.box1.show()
        self.window.show()

    def get_keys(self):

        self.rsa_controller1 = RsaController('c', pubfile=self.pub_a)
        self.rsa_controller2 = RsaController('m', privfile=self.priv_b)

        # Programma gebruikt Private_B om File_2 te decrypteren,
        # en zo de symmetrische key te verkrijgen
        cipher = self.rsa_controller2.decrypt_private(open(self.file_2, 'r').read())
        self.aes_controller = AesController(cipher=cipher)

        # Programma gebruikt die symmetrische key om File_1 te decrypteren
        # om terug de verstuurde boodschap te verkrijgen, en toont die
        # boodschap dan ook op het scherm
        self.text = self.aes_controller.decrypt(open(self.file_1, 'r').read())

        # Programma berekent zelf de hash van die boodschap
        # Programma gebruikt Public_A om File_3 te decrypteren,
        # en zo terug de hash te verkrijgen van de originele file
        self.ok = self.rsa_controller1.verify_signature(self.text, open(self.file_3).read())

        # Programma controleert of de gedecrypteerde hash,
        # en de zelf berekende hash overeenkomen,
        # en geeft een boodschap indien ok of niet
        # self.ok = (orig_hash == own_hash)

    def main(self):
        gtk.main()
