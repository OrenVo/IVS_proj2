from PyQt5 import QtWidgets, QtCore
from deus_gui import Ui_MainWindow
import deus_math_lib
from PyQt5.QtGui import *
import os

class Deus_Window(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
