from PyQt5 import QtWidgets, QtCore
from deus_gui import Ui_MainWindow
import deus_math_lib
from PyQt5.QtGui import *
import os

err = False
a = 0
op = ""
ans = ""

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
        self.AnsBtn.clicked.connect(self.ansClick)
        #Unary operators
        self.RndBtn.clicked.connect(self.unary_op)
        self.AbsBtn.clicked.connect(self.unary_op)
        self.FactBtn.clicked.connect(self.unary_op)
        self.PercBtn.clicked.connect(self.unary_op)
        self.PromBtn.clicked.connect(self.unary_op)
        #Arithmetic operators
        self.AddBtn.clicked.connect(self.arithmetic_op)
        self.DivBtn.clicked.connect(self.arithmetic_op)
        self.MulBtn.clicked.connect(self.arithmetic_op)
        self.SubBtn.clicked.connect(self.arithmetic_op)
        self.PowBtn.clicked.connect(self.arithmetic_op)
        self.RootBtn.clicked.connect(self.arithmetic_op)
        self.LogBtn.clicked.connect(self.arithmetic_op)
        self.EqualsBtn.setAutoDefault(True)
        self.EqualsBtn.clicked.connect(self.equal)

        self.DeusVult.clicked.connect(self.Deus)

    def Keyboard_pressed(self):
        global err
        global ans
        if err == True:
            err = False
            self.Input.clear()
        if str(ans) == self.Input.text():
            self.Input.clear()
        newinput = self.Input.text() + self.sender().text()
        self.Input.setText(newinput)


    def bckspace(self):
        global err
        if err == True:
            err = False
            self.Input.clear()
            return
        newinput = self.Input.text()
        self.Input.setText(newinput[:-1])

    def unary_op(self):
        operator = self.sender().text()
        global err
        global ans
        val = self.Input.text()
        if err == True:
            return
        if val == "e":
            val = deus_math_lib.deus_e()
        elif val == "π":
            val = deus_math_lib.deus_pi()

        try:
            if operator == "Rnd":
                res = deus_math_lib.deus_rnd()
            elif operator == "x!":
                val = int(val)
                if val > 170:
                    err = True
                    self.Input.setText("Over the limit!!")
                    return
                res = float(deus_math_lib.deus_fact_ite(val))

            elif operator == "abs":
                val = float(val)
                res = deus_math_lib.deus_abs(val)

            elif operator == "%":
                val = float(val)
                res = str(deus_math_lib.deus_percent(val)) + "%"

            elif operator == "‰":
                val = float(val)
                res = str(deus_math_lib.deus_promille(val)) + "‰"

        except Exception as e:
            print(str(e))
            err = True
            self.Input.setText("Error")
        else:
            ans = res
            self.Input.setText(str(res))

    def arithmetic_op(self):
        operator = self.sender().text()
        global err
        global a
        global op
        if err == True:
            return
        if operator == "-" and (self.Input.text() == "" or err == True):
            err = False
            self.Input.setText("-")
            return
        op = operator

        val = self.Input.text().replace(",", ".")
        self.Input.clear()

        if val == "π":
            a = deus_math_lib.deus_pi()
            return
        if val == "e":
            a = deus_math_lib.deus_e()
            return
        try:
            val = float(val)
        except:
            err = True
            self.Input.setText("Error")
            return
        a = val
        return

    def equal(self):
        global err
        global a
        global op
        global ans
        if err == True:
            err = False
            self.Input.clear()
            return

        val = self.Input.text().replace(",", ".")
        if val == "e":
            b = deus_math_lib.deus_e()
        elif val == "π":
            b = deus_math_lib.deus_pi()
        else:
            try:
                b = float(val)
            except:
                err = True
                self.Input.setText("Error")
                return
        try:
            if op == "+":
                ans = deus_math_lib.deus_sum(a, b)
                self.Input.setText(str(ans))
            elif op == "-":
                ans = deus_math_lib.deus_sub(a, b)
                self.Input.setText(str(ans))
            elif op == "×":
                ans = deus_math_lib.deus_mult(a, b)
                self.Input.setText(str(ans))
            elif op == "÷":
                ans = deus_math_lib.deus_div(a, b)
                self.Input.setText(str(ans))
            elif op == "x^n":
                ans = float(deus_math_lib.deus_pow(a, b))
                self.Input.setText(str(ans))
            elif op == "√x":
                ans = deus_math_lib.deus_root(b, a)
                self.Input.setText(str(ans))
            elif op == "log":
                ans = deus_math_lib.deus_log(b, a)
                self.Input.setText(str(ans))
            elif op == "" and val == "e":
                self.Input.setText(str(b))
            elif op == "" and val == "π":
                self.Input.setText(str(b))

            if op == "":
                ans = b
            op = ""
        except:
            err = True
            self.Input.setText("Error")


    def ansClick(self):
        global ans
        self.Input.setText(str(ans))

        pres = False
    def Deus(self):
        self.Input.setText(str(deus_math_lib.deus_vult()))
