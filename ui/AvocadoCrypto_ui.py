# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AvocadoCrypto.ui'
#
# Created: Thu Dec 17 10:44:09 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

from ui.ui_controller import ui_controller


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(511, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStatusTip("")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ButtonDecrypt = QtGui.QPushButton(Dialog)
        self.ButtonDecrypt.setEnabled(False)
        self.ButtonDecrypt.setGeometry(QtCore.QRect(410, 260, 81, 27))
        self.ButtonDecrypt.setObjectName("ButtonDecrypt")
        self.ButtonEncrypt = QtGui.QPushButton(Dialog)
        self.ButtonEncrypt.setEnabled(False)
        self.ButtonEncrypt.setGeometry(QtCore.QRect(320, 260, 81, 27))
        self.ButtonEncrypt.setObjectName("ButtonEncrypt")
        self.groupBoxSource = QtGui.QGroupBox(Dialog)
        self.groupBoxSource.setGeometry(QtCore.QRect(270, 10, 181, 61))
        self.groupBoxSource.setObjectName("groupBoxSource")
        self.radioButtonTextSource = QtGui.QRadioButton(self.groupBoxSource)
        self.radioButtonTextSource.setGeometry(QtCore.QRect(10, 30, 61, 22))
        self.radioButtonTextSource.setChecked(False)
        self.radioButtonTextSource.setObjectName("radioButtonTextSource")
        self.radioButtonFileSource = QtGui.QRadioButton(self.groupBoxSource)
        self.radioButtonFileSource.setGeometry(QtCore.QRect(101, 30, 81, 22))
        self.radioButtonFileSource.setChecked(True)
        self.radioButtonFileSource.setObjectName("radioButtonFileSource")
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 231, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tabWidget = QtGui.QTabWidget(self.groupBox_2)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 231, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tabTools = QtGui.QWidget()
        self.tabTools.setObjectName("tabTools")
        self.ButtonGenKeys = QtGui.QPushButton(self.tabTools)
        self.ButtonGenKeys.setGeometry(QtCore.QRect(10, 10, 191, 27))
        self.ButtonGenKeys.setObjectName("ButtonGenKeys")
        self.ButtonGenAes = QtGui.QPushButton(self.tabTools)
        self.ButtonGenAes.setGeometry(QtCore.QRect(10, 50, 191, 27))
        self.ButtonGenAes.setObjectName("ButtonGenRsa")
        self.ButtonGenOwnRsa = QtGui.QPushButton(self.tabTools)
        self.ButtonGenOwnRsa.setGeometry(QtCore.QRect(10, 100, 191, 27))
        self.ButtonGenOwnRsa.setObjectName("ButtonGenOwnAes")
        self.ButtonGenResRsa = QtGui.QPushButton(self.tabTools)
        self.ButtonGenResRsa.setGeometry(QtCore.QRect(10, 130, 191, 27))
        self.ButtonGenResRsa.setObjectName("ButtonGenResAes")
        self.ButtonSwitchRsa = QtGui.QPushButton(self.tabTools)
        self.ButtonSwitchRsa.setEnabled(False)
        self.ButtonSwitchRsa.setGeometry(QtCore.QRect(10, 170, 191, 27))
        self.ButtonSwitchRsa.setObjectName("ButtonSwitchAes")
        self.tabWidget.addTab(self.tabTools, "")
        self.tabAes = QtGui.QWidget()
        self.tabAes.setObjectName("tabAes")
        self.groupBoxOwnAes = QtGui.QGroupBox(self.tabAes)
        self.groupBoxOwnAes.setGeometry(QtCore.QRect(0, 0, 221, 91))
        self.groupBoxOwnAes.setObjectName("groupBoxOwnAes")
        self.lineOwnPrivate = QtGui.QLineEdit(self.groupBoxOwnAes)
        self.lineOwnPrivate.setGeometry(QtCore.QRect(82, 20, 131, 27))
        self.lineOwnPrivate.setObjectName("lineOwnPrivate")
        self.lineOwnPublic = QtGui.QLineEdit(self.groupBoxOwnAes)
        self.lineOwnPublic.setGeometry(QtCore.QRect(80, 60, 131, 27))
        self.lineOwnPublic.setObjectName("lineOwnPublic")
        self.label = QtGui.QLabel(self.groupBoxOwnAes)
        self.label.setGeometry(QtCore.QRect(20, 30, 56, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBoxOwnAes)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 56, 17))
        self.label_2.setObjectName("label_2")
        self.groupBoxResRsa = QtGui.QGroupBox(self.tabAes)
        self.groupBoxResRsa.setGeometry(QtCore.QRect(0, 100, 221, 101))
        self.groupBoxResRsa.setObjectName("groupBoxResAes")
        self.lineResPrivate = QtGui.QLineEdit(self.groupBoxResRsa)
        self.lineResPrivate.setGeometry(QtCore.QRect(80, 20, 131, 27))
        self.lineResPrivate.setObjectName("lineResPrivate")
        self.lineResPublic = QtGui.QLineEdit(self.groupBoxResRsa)
        self.lineResPublic.setGeometry(QtCore.QRect(80, 60, 131, 27))
        self.lineResPublic.setObjectName("lineResPublic")
        self.label_3 = QtGui.QLabel(self.groupBoxResRsa)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 56, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBoxResRsa)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 56, 17))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tabAes, "")
        self.plainTextEdit = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(270, 140, 221, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.ButtonFileSelect = QtGui.QPushButton(Dialog)
        self.ButtonFileSelect.setGeometry(QtCore.QRect(270, 70, 81, 27))
        self.ButtonFileSelect.setObjectName("ButtonFileSelect")
        self.labelSelectedFile = QtGui.QLabel(Dialog)
        self.labelSelectedFile.setGeometry(QtCore.QRect(280, 110, 211, 17))
        self.labelSelectedFile.setObjectName("labelSelectedFile")
        self.checkBoxMd5 = QtGui.QCheckBox(Dialog)
        self.checkBoxMd5.setGeometry(QtCore.QRect(370, 70, 100, 22))
        self.checkBoxMd5.setObjectName("checkBox")

        self.controller = ui_controller(self)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        # QtCore.QObject.connect(self.ButtonDecrypt, QtCore.SIGNAL("clicked()"), Dialog.exec)
        # QtCore.QObject.connect(self.ButtonEncrypt, QtCore.SIGNAL("clicked()"), Dialog.exec)

        # Source
        self.radioButtonFileSource.clicked.connect(self.controller.set_source)
        self.radioButtonTextSource.clicked.connect(self.controller.set_source)
        self.ButtonFileSelect.clicked.connect(self.controller.select_source_file)
        self.ButtonDecrypt.clicked.connect(self.controller.decrypt)
        self.ButtonEncrypt.clicked.connect(self.controller.encrypt)

        # Keys
        # Tools
        self.ButtonGenKeys.clicked.connect(self.controller.generate_all_keys)
        self.ButtonGenAes.clicked.connect(self.controller.generate_aes)
        self.ButtonGenOwnRsa.clicked.connect(self.controller.generate_own_rsa)
        self.ButtonGenResRsa.clicked.connect(self.controller.generate_res_rsa)
        self.ButtonSwitchRsa.clicked.connect(self.controller.switch_rsa)
        self.checkBoxMd5.clicked.connect(self.controller.toggle_md5())

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QtGui.QApplication.translate("Dialog", "AvocadoCrypto", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonDecrypt.setText(
            QtGui.QApplication.translate("Dialog", "Decrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonEncrypt.setText(
            QtGui.QApplication.translate("Dialog", "Encrypt", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxSource.setTitle(
            QtGui.QApplication.translate("Dialog", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonTextSource.setText(
            QtGui.QApplication.translate("Dialog", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonFileSource.setText(
            QtGui.QApplication.translate("Dialog", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Keys", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonGenKeys.setText(
            QtGui.QApplication.translate("Dialog", "Generate all keys", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonGenAes.setText(
            QtGui.QApplication.translate("Dialog", "Generate AES", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonGenOwnRsa.setText(
            QtGui.QApplication.translate("Dialog", "Generate own RSA", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonGenResRsa.setText(QtGui.QApplication.translate("Dialog", "Generate Sender/Receiver RSA", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.ButtonSwitchRsa.setText(QtGui.QApplication.translate("Dialog", "Switch own <> Sender/Receiver", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTools),
                                  QtGui.QApplication.translate("Dialog", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxOwnAes.setTitle(
            QtGui.QApplication.translate("Dialog", "Own RSA", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Private:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Public:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBoxResRsa.setTitle(
            QtGui.QApplication.translate("Dialog", "Sender / Receiver RSA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Private:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Public:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAes),
                                  QtGui.QApplication.translate("Dialog", "RSA", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonFileSelect.setText(
            QtGui.QApplication.translate("Dialog", "Select File", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSelectedFile.setText(
            QtGui.QApplication.translate("Dialog", "(no file selected)", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMd5.setText(QtGui.QApplication.translate("Dialog", "MD5", None, QtGui.QApplication.UnicodeUTF8))