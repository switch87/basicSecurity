import sys

from PySide.QtGui import QMainWindow, QApplication

from ui.mainwindow import MainWindow


class MyApplication(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setup_ui(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
