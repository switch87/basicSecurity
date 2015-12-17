#!/usr/bin/python

# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import *
from PySide.QtCore import *
from AvocadoCrypto_ui import *

class MyApplication(QtGui.QMainWindow, Ui_Dialog):
        def __init__(self, parent=None):
                super(MyApplication, self).__init__(parent)
                self.setupUi(self)

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        window = MyApplication()
        window.show()
        sys.exit(app.exec_())