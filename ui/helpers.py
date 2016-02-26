import os
import re

from PySide import QtGui
from tr import tr


def get_file_name(file_dir):
    return re.split(r'/', file_dir)[-1]


def save_to_file(data, file):
    if file_exists(file):
        open(file, 'w').write(data)


def select_file(namefilter=None):
    dialog = QtGui.QFileDialog()
    dialog.setFileMode(QtGui.QFileDialog.AnyFile)
    dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, False)
    if namefilter:
        dialog.setNameFilter(namefilter)
    dialog.exec_()
    return dialog.selectedFiles()[0] or None


def file_exists(file):
    if not os.path.isfile(file) and not os.path.isdir(file):
        os.mknod(file)
    elif os.path.isdir(file):
        return False
    return True
