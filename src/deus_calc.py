from PyQt5 import QtWidgets, QtCore
from deus_gui import Ui_MainWindow
import deus_math_lib
from PyQt5.QtGui import *
import os

err = False

class Deus_Window(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        #Keyboard handling
        self.ZeroBtn.clicked.connect(self.Keyboard_pressed)
        self.OneBtn.clicked.connect(self.Keyboard_pressed)
        self.TwoBtn.clicked.connect(self.Keyboard_pressed)
        self.ThreeBtn.clicked.connect(self.Keyboard_pressed)
        self.FourBtn.clicked.connect(self.Keyboard_pressed)
        self.FiveBtn.clicked.connect(self.Keyboard_pressed)
        self.SixBtn.clicked.connect(self.Keyboard_pressed)
        self.SevenBtn.clicked.connect(self.Keyboard_pressed)
        self.EightBtn.clicked.connect(self.Keyboard_pressed)
        self.NineBtn.clicked.connect(self.Keyboard_pressed)
        self.DotBtn.clicked.connect(self.Keyboard_pressed)
        self.EulerBtn.clicked.connect(self.Keyboard_pressed)
        self.PiBtn.clicked.connect(self.Keyboard_pressed)
        self.BackspaceBtn.clicked.connect(self.bckspace)
        #self.AnsBtn.clicked.connect(self.button_pressed)
        #Unary operators
        self.RndBtn.clicked.connect(self.unary_op)
        self.AbsBtn.clicked.connect(self.unary_op)
        self.FactBtn.clicked.connect(self.unary_op)
        self.PercBtn.clicked.connect(self.unary_op)
        self.PromBtn.clicked.connect(self.unary_op)
        #Arithmetic operators
        """self.DivBtn.clicked.connect(self.button_pressed)
        self.MulBtn.clicked.connect(self.button_pressed)
        self.SubBtn.clicked.connect(self.button_pressed)
        self.AddBtn.clicked.connect(self.button_pressed)
        self.PowBtn.clicked.connect(self.button_pressed)
        self.RootBtn.clicked.connect(self.button_pressed)
        self.LogBtn.clicked.connect(self.button_pressed)

        self.EqualsBtn.clicked.connect(self.button_pressed)"""



    def Keyboard_pressed(self):
        btn = self.sender()
        global err
        if err == True:
            err = False
            self.Input.setText("")
        newinput = self.Input.text() + self.sender().text()
        self.Input.setText(newinput)


    def bckspace(self):
        input = self.Input.text()
        self.Input.setText(input[:-1])

    def unary_op(self):
        btn = self.sender()
        operator = self.sender().text()
        res = "Error"
        global err
        val = self.Input.text()

        if operator == "Rnd":
            res = deus_math_lib.deus_rnd()

        elif operator == "x!":
            try:
                val = int(val)
                res = deus_math_lib.deus_fact_ite(val)
            except Exception as e:
                err = True
                self.Input.setText("Error")
                return
        elif operator == "abs":
            try:
                val = float(val)
                res = deus_math_lib.deus_abs(val)
            except Exception as e:
                err = True
                self.Input.setText("Error")

        elif operator == "%":
            try:
                val = float(val)
            except Exception as e:
                err = True
                self.Input.setText("Error")
            res = str(deus_math_lib.deus_percent(val)) + "%"
            err = True

        elif operator == "‰":
            try:
                val = float(val)
            except Exception as e:
                err = True
                self.Input.setText("Error")
            res = str(deus_math_lib.deus_promille(val)) + "‰"
            err = True

        self.Input.setText(str(res))
