import sys
import unittest
from PyQt4 import QtGui

from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt


from ui.gui import MainWindow


class UiTest(unittest.TestCase):
    def test_user_can_generate_new_aes(self):
        app = QtGui.QApplication(sys.argv)
        window = MainWindow()
        QTest.mouseClick(window.menuBar(), Qt.LeftButton)
        assert window.aes is not None
