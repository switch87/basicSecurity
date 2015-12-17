import os

from PySide import QtGui

from CryptoController.Aes import AesController
from CryptoController.Rsa import RsaController
from ui.helpers import get_file_name, select_file, save_to_file, check_file


class UiController():
    def __init__(self, ui):
        self.ui = ui
        self.aes = None
        self.fileName = None
        self.own_rsa_priv = None
        self.own_rsa_pub = None
        self.rec_rsa_pub = None
        self.rec_rsa_priv = None

        self.md5 = False

        self.update_ui()

    def update_ui(self):
        # check if keys can be switched
        self.ui.button_switch_rsa.setEnabled(
                True if (
                    self.rec_rsa_priv and self.rec_rsa_pub and
                    self.own_rsa_priv and self.own_rsa_pub)
                else False)

        self.ui.button_decrypt.setEnabled(True if self.aes and self.has_data() else False)
        self.ui.button_encrypt.setEnabled(True if self.aes and self.has_data() else False)

        self.ui.line_own_public.setText(self.own_rsa_pub)
        self.ui.line_own_private.setText(self.own_rsa_priv)
        self.ui.line_rec_public.setText(self.rec_rsa_pub)
        self.ui.line_rec_private.setText(self.rec_rsa_priv)

    def set_source(self):
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
        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.ExistingFiles)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, False)
        dialog.exec_()
        if len(dialog.selectedFiles()) != 0:
            self.fileName = dialog.selectedFiles()[0]
            self.ui.label_selected_file.setText(get_file_name(self.fileName))
        self.update_ui()

    def generate_all_keys(self):
        self.generate_aes()
        self.generate_own_rsa()
        self.generate_res_rsa()

    def generate_aes(self):
        self.aes = AesController()
        self.update_ui()

    def generate_own_rsa(self):
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

    def generate_res_rsa(self):
        self.res_rsa = RsaController('m')
        dialog = QtGui.QInputDialog()

        dialog.setTextValue("Public_B")
        dialog.setLabelText("Sender/receiver public key:")
        dialog.exec_()
        self.rec_rsa_pub = dialog.textValue()

        dialog.setTextValue("Private_B")
        dialog.setLabelText("Sender/receiver private key:")
        dialog.exec_()
        self.rec_rsa_priv = dialog.textValue()

        self.res_rsa.save_keys(self.rec_rsa_pub, self.rec_rsa_priv)
        self.update_ui()

    def decrypt_file(self):
        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.AnyFile)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, False)
        dialog.exec_()
        if len(dialog.selectedFiles()) != 0:
            out_file = dialog.selectedFiles()[0]
            if not os.path.isfile(out_file):
                os.mknod(out_file)
            self.aes.decrypt_file(open(self.fileName, 'rb'), open(out_file, 'wb'))

    def encrypt_file(self):
        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.AnyFile)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, False)
        dialog.exec_()
        if len(dialog.selectedFiles()) != 0:
            out_file = dialog.selectedFiles()[0]
            if check_file(out_file):
                self.aes.encrypt_file(open(self.fileName, 'rb'), open(out_file, 'wb'))

    def encrypt(self):
        if self.ui.radio_button_text_source.isChecked():
            self.encrypt_text()
        else:
            self.encrypt_file()

    def decrypt(self):
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
        data = self.aes.encrypt(self.ui.plain_text_edit.toPlainText())
        file = select_file(QtGui.QFileDialog.AnyFile)
        if file:
            save_to_file(data, file)

    def decrypt_text(self):
        data = self.aes.decrypt(self.ui.plain_text_edit.toPlainText())
        file = select_file(QtGui.QFileDialog.AnyFile)
        if file:
            if self.md5:
                rsa = RsaController('m', privfile=open(self.own_rsa_priv), pubfile=open(self.own_rsa_pub))
                save_to_file(rsa.sign_with_md5(data), file + "_md5")
            save_to_file(data, file)

    def switch_rsa(self):
        temp_private = self.rec_rsa_priv
        temp_public = self.rec_rsa_pub
        self.rec_rsa_priv = self.own_rsa_priv
        self.rec_rsa_pub = self.own_rsa_pub
        self.own_rsa_priv = temp_private
        self.own_rsa_pub = temp_public
        self.update_ui()

    def toggle_md5(self):
        self.md5 = not self.md5
