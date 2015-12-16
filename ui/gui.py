import sys
from PyQt4 import QtGui

from CryptoController.Aes import AesController
from CryptoController.Rsa import RsaController


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

        self.prim_rsa_file1 = "Public_A"
        self.prim_rsa_file2 = "Private_A"
        self.sec_rsa_file1 = "Public_B"
        self.sec_rsa_file2 = "Private_B"

    def initUI(self):
        self.statusBar()
        self.init_menu()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('AvocadoCrypto')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()

    def init_menu(self):
        self.aesAction = QtGui.QAction('Generate Aes', self)
        self.aesAction.triggered.connect(self.init_aes)

        primaryRsaAction = QtGui.QAction('Generate primary RSA',self)
        primaryRsaAction.triggered.connect(self.init_primary_rsa)

        secondaryRsaAction = QtGui.QAction('Generate secondary RSA',self)
        secondaryRsaAction.triggered.connect(self.init_secondary_rsa)

        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(self.aesAction)
        fileMenu.addAction(primaryRsaAction)
        fileMenu.addAction(secondaryRsaAction)
        fileMenu.addAction(exitAction)

    def init_aes(self):
        self.aes = AesController()
        self.statusBar().showMessage('New AES generated')

    def init_primary_rsa(self):
        self.prim_rsa = RsaController('m')
        self.prim_rsa.save_keys(self.prim_rsa_file1, self.prim_rsa_file2)
        self.statusBar().showMessage('New primary RSA generated')

    def init_secondary_rsa(self):
        self.prim_rsa = RsaController('m')
        self.prim_rsa.save_keys(self.sec_rsa_file1, self.sec_rsa_file2)
        self.statusBar().showMessage('New secondary RSA generated')

def main():
    app = QtGui.QApplication(sys.argv)
    x = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
