import os
import re
from PySide import QtGui


def get_file_name(file_dir):
    return re.split(r'/', file_dir)[-1]

def save_to_file(data, file):
    check_file(file)
    open(file, 'w').write(data)

def select_file(QFileDialo):
    dialog = QtGui.QFileDialog()
    dialog.setFileMode(QtGui.QFileDialog.AnyFile)
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, False)
    dialog.exec_()
    return dialog.selectedFiles()[0] or None

def check_file(file):
    if not os.path.isfile(file):
                os.mknod(file)