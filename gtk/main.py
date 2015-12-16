import gtk
import pygtk

from ui.Decrypt import DecryptionWindow

from gtk.Encrypt import EncryptionWindow

pygtk.require('2.0')


class MainWindow:
    def encrypt(self, widget):
        EncryptionWindow().main()

    def decrypt(self, widget):
        DecryptionWindow().main()

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("AvocadoCrypto")
        self.window.set_icon_from_file('icon.png')
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(10)

        self.box1 = gtk.HBox(False, 0)
        self.window.add(self.box1)

        self.button1 = gtk.Button("Encrypt")
        self.button1.connect("clicked", self.encrypt)
        self.box1.pack_start(self.button1, True, True, 0)
        self.button1.show()

        self.button2 = gtk.Button("Decrypt")
        self.button2.connect("clicked", self.decrypt)
        self.box1.pack_start(self.button2, True, True, 0)
        self.button2.show()

        self.box1.show()
        self.window.show()

    def main(self):
        gtk.main()
