import os

from PySide import QtGui, QtCore
from rsa import VerificationError

from CryptoController.Aes import AesController
from CryptoController.Rsa import RsaController
from ui.helpers import get_file_name, select_file, save_to_file, make_file_exist, show_message


class UiController():
    def __init__(self, ui):
        self.rec_rsa = None
        self.own_rsa = None
        self.ui = ui
        self.aes = None
        self.fileName = None
        self.own_rsa_priv = None
        self.own_rsa_pub = None
        self.rec_rsa_pub = None
        self.rec_rsa_priv = None

        self.md5 = False
        self.stegano = False
        
        self.stegano_image = "/home/switch87/workplace/pythonDjango/basicSecurity/icon.png"
        self.set_stegano_preview()

        self.update_ui()

    def update_ui(self):
        """
        Update userinterface after changes

            button_switch_rsa  enabled     bool
            button_decrypt     enabled     bool
            button_encrypt     enabled     bool
            button_save_aes
            button_load_aes
            line_own_public    text        string
            line_own_private   text        string
            line_rec_public    text        string
            kine_rec_private   text        string
        """

        # check if keys can be switched
        self.ui.button_switch_rsa.setEnabled(
            True if (
                self.rec_rsa_priv and self.rec_rsa_pub and
                self.own_rsa_priv and self.own_rsa_pub)
            else False)

        self.ui.button_decrypt.setEnabled(True if self.aes else False)
        self.ui.button_encrypt.setEnabled(True if self.aes else False)

        self.ui.button_save_aes.setEnabled(True if self.aes and self.rec_rsa_pub else False)
        self.ui.button_load_aes.setEnabled(True if self.own_rsa_priv else False)

        self.ui.button_image_select.setEnabled(True if self.ui.radio_button_file_source.isChecked() and self.stegano
                                          else False)

        self.ui.line_own_public.setText(self.own_rsa_pub)
        self.ui.line_own_private.setText(self.own_rsa_priv)
        self.ui.line_rec_public.setText(self.rec_rsa_pub)
        self.ui.line_rec_private.setText(self.rec_rsa_priv)

    def set_source(self):
        """
        Togge between file and text source
        """

        if self.ui.radio_button_file_source.isChecked():
            self.ui.radio_button_text_source.setChecked(False)
            self.ui.button_file_select.setEnabled(True)
            self.ui.plain_text_edit.setEnabled(False)
            self.ui.label_selected_file.setEnabled(True)
        else:
            self.ui.radio_button_file_source.setChecked(False)
            self.ui.button_file_select.setEnabled(False)
            self.ui.plain_text_edit.setEnabled(True)
            self.ui.label_selected_file.setEnabled(False)
        self.update_ui()

    def select_source_file(self):
        """
        Select file wich will be used as source
        Check if selected file does exist
        """

        file = select_file()
        if file:
            self.fileName = file
            self.ui.label_selected_file.setText(get_file_name(self.fileName))
            self.update_ui()

    def select_own_private_file(self):
        """
        select file for own private RSA key
        :return: None
        """

        file = select_file()
        if file:
            self.own_rsa_priv = file
            if self.own_rsa:
                self.own_rsa.update_keys(privfile=self.own_rsa_priv)
            else:
                self.own_rsa = RsaController('m', privfile=self.own_rsa_priv, pubfile=self.own_rsa_pub)
            self.update_ui()

    def select_own_public_file(self):
        """
        select file for own public RSA key
        :return: None
        """

        file = select_file()
        if file:
            self.own_rsa_pub = file
            if self.own_rsa:
                self.own_rsa.update_keys(pubfile=self.own_rsa_pub)
            else:
                self.own_rsa = RsaController('m', privfile=self.own_rsa_priv, pubfile=self.own_rsa_pub)
            self.update_ui()

    def select_rec_private_file(self):
        """
        select file for receiver private RSA key
        :return: None
        """

        file = select_file()
        if file:
            self.rec_rsa_priv = file
            if self.rec_rsa:
                self.rec_rsa.update_keys(privfile=self.rec_rsa_priv)
            else:
                self.rec_rsa = RsaController('m', privfile=self.rec_rsa_priv, pubfile=self.rec_rsa_pub)
            self.update_ui()

    def select_rec_public_file(self):
        """
        select file for receiver public RSA key
        :return: None
        """

        file = select_file()
        if file:
            self.rec_rsa_pub = file
            if self.rec_rsa:
                self.rec_rsa.update_keys(pubfile=self.rec_rsa_pub)
            else:
                self.rec_rsa = RsaController('m', privfile=self.rec_rsa_priv, pubfile=self.rec_rsa_pub)
            self.update_ui()

    def generate_all_keys(self):
        """
        Generate all RSA keys and a new aes key
        """

        self.generate_aes()
        self.generate_own_rsa()
        self.generate_rec_rsa()

    def generate_aes(self):
        """
        Generate aes key

        this key will not automatically be saved to a file!
        """

        self.aes = AesController()
        self.update_ui()

    def generate_own_rsa(self):
        """
        Generate own RSA keys and save them to files.
        Show dialogs to decide how to name the key-files.
        """

        self.own_rsa = RsaController('m')
        dialog = QtGui.QInputDialog()

        dialog.setTextValue("Public_A")
        dialog.setLabelText("Your public key:")
        dialog.exec_()
        self.own_rsa_pub = dialog.textValue()

        dialog.setTextValue("Private_A")
        dialog.setLabelText("Your private key:")
        dialog.exec_()
        self.own_rsa_priv = dialog.textValue()

        self.own_rsa.save_keys(self.own_rsa_pub, self.own_rsa_priv)
        self.update_ui()

    def generate_rec_rsa(self):
        """
        Generate receiver RSA keys and save them to files.
        Show dialogs to decide how to name the key-files.

        The private key will also be created, this is not advised in the real world!
        """

        self.rec_rsa = RsaController('m')
        dialog = QtGui.QInputDialog()

        dialog.setTextValue("Public_B")
        dialog.setLabelText("Sender/receiver public key:")
        dialog.exec_()
        self.rec_rsa_pub = dialog.textValue()

        dialog.setTextValue("Private_B")
        dialog.setLabelText("Sender/receiver private key:")
        dialog.exec_()
        self.rec_rsa_priv = dialog.textValue()

        self.rec_rsa.save_keys(self.rec_rsa_pub, self.rec_rsa_priv)
        self.update_ui()

    def decrypt_file(self):
        """
        Decrypt selected source file and ask for file to save decryption.

        If MD5 checked compare hash
        """

        out_file = select_file()
        if out_file and make_file_exist(out_file):
            if self.stegano:
                self.aes.extract_from_image(self.fileName, self.fileName+".tmp")
                self.aes.decrypt_file(open(self.fileName+".tmp", 'rb'), open(out_file, 'wb'))
            else:
                self.aes.decrypt_file(open(self.fileName, 'rb'), open(out_file, 'wb'))

            if self.md5:
                try:
                    md5_file = self.fileName + ".md5"
                    self.rec_rsa.verify_signature(open(out_file, 'rb').read(), open(md5_file, 'rb').read())
                    show_message("The MD5 signature passed")
                except VerificationError:
                    show_message("VerificationError: The MD5 signature does not mach.")

    def encrypt_file(self):
        """
        Encrypt selected source file and ask for file to save encryption.

        If MD5 checked; generate hash
        """

        out_file = select_file()
        if make_file_exist(out_file):
            if self.stegano:
                self.aes.encrypt_file(open(self.fileName, 'rb'), open(out_file+'.tmp', 'wb'))
                self.aes.save_in_image(open(out_file+'.tmp','rb').read(), self.stegano_image, out_file)
            else:
                self.aes.encrypt_file(open(self.fileName, 'rb'), open(out_file, 'wb'))

            if self.md5:
                md5_file = out_file + ".md5"
                save_to_file(self.own_rsa.sign_with_md5(open(self.fileName, 'rb')), md5_file)

    def encrypt(self):
        """
        decide how to encrypt according to source type
        """

        if self.ui.radio_button_text_source.isChecked():
            self.encrypt_text()
        else:
            self.encrypt_file()

    def decrypt(self):
        """
        decide how to decrypt according to source type
        """

        if self.ui.radio_button_text_source.isChecked():
            self.decrypt_text()
        else:
            self.decrypt_file()

    def has_data(self):
        # als er een bronbestand geselecteerd is return True
        # als er text ingegeven is return True
        return True if (self.ui.radio_button_file_source.isChecked() and self.ui.label_selected_file.text() !=
                        QtGui.QApplication.translate("Dialog", "(no file selected)", None,
                                                     QtGui.QApplication.UnicodeUTF8)) or \
                       (self.ui.radio_button_text_source.isChecked() and
                        len(self.ui.plain_text_edit.toPlainText()) > 0) else False

    def encrypt_text(self):
        """
        Encrypt content of plain_text_edit and place encrypted string back in plain_text_edit.
        """

        data = self.aes.encrypt(self.ui.plain_text_edit.toPlainText())

        self.ui.plain_text_edit.setPlainText(data)

        # file = select_file(QtGui.QFileDialog.AnyFile)
        # if file:
        #     save_to_file(data, file)

    def decrypt_text(self):
        """
        Decrypt content of plain_text_edit and place decrypted string back in plain_text_edit.
        """

        data = self.aes.decrypt(self.ui.plain_text_edit.toPlainText())

        self.ui.plain_text_edit.setPlainText(data)

        # file = select_file(QtGui.QFileDialog.AnyFile)
        # if file:
        #     if self.md5:
        #         rsa = RsaController('m', privfile=open(self.own_rsa_priv), pubfile=open(self.own_rsa_pub))
        #         save_to_file(rsa.sign_with_md5(data), file + "_md5")
        #     save_to_file(data, file)

    def switch_rsa(self):
        """
        Switch own and receivers RSA keys.

        Returns error if receiver private key is not assigned.
        """

        if self.rec_rsa_priv == None:
            pass
            # todo: show message there is no private key to be assigned
        else:
            temp_private = self.rec_rsa_priv
            temp_public = self.rec_rsa_pub
            self.rec_rsa_priv = self.own_rsa_priv
            self.rec_rsa_pub = self.own_rsa_pub
            self.own_rsa_priv = temp_private
            self.own_rsa_pub = temp_public
            self.own_rsa.update_keys(privfile=self.own_rsa_priv, pubfile=self.own_rsa_pub)
            self.rec_rsa.update_keys(privfile=self.rec_rsa_priv, pubfile=self.rec_rsa_pub)
            self.update_ui()

    def toggle_md5(self):
        """
        toggle if md5 should be used.

        md5 is only used for file encryption/decryption.
        """

        self.md5 = not self.md5

    def load_aes(self):
        """
        Decrypt AES secret with own private key and generate AES key
        :return:
        """

        filename = select_file()
        if make_file_exist(filename):
            secret = self.own_rsa.decrypt(open(filename, 'rb').read())
            self.aes = AesController(secret=secret)
            self.update_ui()

    def save_aes(self):
        """
        Encrypt aes secret with receivers public key and save it to file
        :return:
        """

        filename = select_file()
        if filename:
            save_to_file(self.rec_rsa.encrypt(self.aes.secret), filename)

    def toggle_stegano(self):
        self.stegano = not self.stegano
        self.update_ui()

    def select_image(self):
        filename = select_file(namefilter="images (*png *.jpg *.jpeg)")
        if make_file_exist(filename):
            self.stegano_image = filename
            self.set_stegano_preview()

    def set_stegano_preview(self):
        picture = QtGui.QPixmap(self.stegano_image).scaled(QtCore.QSize(280, 190))
        scene = QtGui.QGraphicsScene()

        #scene.setSceneRect(-600,-600, 600,600)
        scene.setSceneRect(0,0, 280, 190)
        scene.addItem(QtGui.QGraphicsPixmapItem(picture))
        view = self.ui.stegano_preview
        view.setScene(scene)
        view.setRenderHint(QtGui.QPainter.Antialiasing)
        view.show()