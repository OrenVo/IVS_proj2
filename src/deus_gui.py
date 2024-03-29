# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc-Gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 577)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 577))
        MainWindow.setMaximumSize(QtCore.QSize(350, 527))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("deus_vult.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Input.sizePolicy().hasHeightForWidth())
        self.Input.setSizePolicy(sizePolicy)
        self.Input.setMinimumSize(QtCore.QSize(320, 80))
        self.Input.setMaximumSize(QtCore.QSize(330, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Input.setFont(font)
        self.Input.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Input.setAcceptDrops(True)
        self.Input.setStyleSheet("border: 2px solid gray")
        self.Input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.Input.setText("")
        self.Input.setFrame(True)
        self.Input.setClearButtonEnabled(False)
        self.Input.setObjectName("Input")
        self.gridLayout_2.addWidget(self.Input, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.SevenBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SevenBtn.sizePolicy().hasHeightForWidth())
        self.SevenBtn.setSizePolicy(sizePolicy)
        self.SevenBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SevenBtn.setFont(font)
        self.SevenBtn.setObjectName("SevenBtn")
        self.gridLayout.addWidget(self.SevenBtn, 6, 0, 1, 1)
        self.FactBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FactBtn.sizePolicy().hasHeightForWidth())
        self.FactBtn.setSizePolicy(sizePolicy)
        self.FactBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.FactBtn.setFont(font)
        self.FactBtn.setObjectName("FactBtn")
        self.gridLayout.addWidget(self.FactBtn, 4, 2, 1, 1)
        self.PiBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PiBtn.sizePolicy().hasHeightForWidth())
        self.PiBtn.setSizePolicy(sizePolicy)
        self.PiBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PiBtn.setFont(font)
        self.PiBtn.setObjectName("PiBtn")
        self.gridLayout.addWidget(self.PiBtn, 5, 1, 1, 1)
        self.OneBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OneBtn.sizePolicy().hasHeightForWidth())
        self.OneBtn.setSizePolicy(sizePolicy)
        self.OneBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.OneBtn.setFont(font)
        self.OneBtn.setObjectName("OneBtn")
        self.gridLayout.addWidget(self.OneBtn, 8, 0, 1, 1)
        self.PowBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PowBtn.sizePolicy().hasHeightForWidth())
        self.PowBtn.setSizePolicy(sizePolicy)
        self.PowBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PowBtn.setFont(font)
        self.PowBtn.setObjectName("PowBtn")
        self.gridLayout.addWidget(self.PowBtn, 3, 0, 1, 1)
        self.BackspaceBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackspaceBtn.sizePolicy().hasHeightForWidth())
        self.BackspaceBtn.setSizePolicy(sizePolicy)
        self.BackspaceBtn.setMinimumSize(QtCore.QSize(80, 50))
        self.BackspaceBtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.BackspaceBtn.setFont(font)
        self.BackspaceBtn.setObjectName("BackspaceBtn")
        self.gridLayout.addWidget(self.BackspaceBtn, 3, 3, 1, 1)
        self.PromBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PromBtn.sizePolicy().hasHeightForWidth())
        self.PromBtn.setSizePolicy(sizePolicy)
        self.PromBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PromBtn.setFont(font)
        self.PromBtn.setObjectName("PromBtn")
        self.gridLayout.addWidget(self.PromBtn, 4, 1, 1, 1)
        self.MulBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MulBtn.sizePolicy().hasHeightForWidth())
        self.MulBtn.setSizePolicy(sizePolicy)
        self.MulBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MulBtn.setFont(font)
        self.MulBtn.setObjectName("MulBtn")
        self.gridLayout.addWidget(self.MulBtn, 7, 3, 1, 1)
        self.SubBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubBtn.sizePolicy().hasHeightForWidth())
        self.SubBtn.setSizePolicy(sizePolicy)
        self.SubBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SubBtn.setFont(font)
        self.SubBtn.setObjectName("SubBtn")
        self.gridLayout.addWidget(self.SubBtn, 6, 3, 1, 1)
        self.FiveBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FiveBtn.sizePolicy().hasHeightForWidth())
        self.FiveBtn.setSizePolicy(sizePolicy)
        self.FiveBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.FiveBtn.setFont(font)
        self.FiveBtn.setObjectName("FiveBtn")
        self.gridLayout.addWidget(self.FiveBtn, 7, 1, 1, 1)
        self.EqualsBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EqualsBtn.sizePolicy().hasHeightForWidth())
        self.EqualsBtn.setSizePolicy(sizePolicy)
        self.EqualsBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.EqualsBtn.setFont(font)
        self.EqualsBtn.setIconSize(QtCore.QSize(30, 30))
        self.EqualsBtn.setAutoDefault(False)
        self.EqualsBtn.setDefault(False)
        self.EqualsBtn.setFlat(False)
        self.EqualsBtn.setObjectName("EqualsBtn")
        self.gridLayout.addWidget(self.EqualsBtn, 9, 3, 1, 1)
        self.PercBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PercBtn.sizePolicy().hasHeightForWidth())
        self.PercBtn.setSizePolicy(sizePolicy)
        self.PercBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.PercBtn.setFont(font)
        self.PercBtn.setObjectName("PercBtn")
        self.gridLayout.addWidget(self.PercBtn, 4, 0, 1, 1)
        self.ZeroBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZeroBtn.sizePolicy().hasHeightForWidth())
        self.ZeroBtn.setSizePolicy(sizePolicy)
        self.ZeroBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ZeroBtn.setFont(font)
        self.ZeroBtn.setFlat(False)
        self.ZeroBtn.setObjectName("ZeroBtn")
        self.gridLayout.addWidget(self.ZeroBtn, 9, 0, 1, 1)
        self.CBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CBtn.sizePolicy().hasHeightForWidth())
        self.CBtn.setSizePolicy(sizePolicy)
        self.CBtn.setMinimumSize(QtCore.QSize(80, 50))
        self.CBtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CBtn.setFont(font)
        self.CBtn.setObjectName("CBtn")
        self.gridLayout.addWidget(self.CBtn, 0, 3, 1, 1)
        self.LogBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogBtn.sizePolicy().hasHeightForWidth())
        self.LogBtn.setSizePolicy(sizePolicy)
        self.LogBtn.setMinimumSize(QtCore.QSize(80, 50))
        self.LogBtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.LogBtn.setFont(font)
        self.LogBtn.setObjectName("LogBtn")
        self.gridLayout.addWidget(self.LogBtn, 3, 2, 1, 1)
        self.DivBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DivBtn.sizePolicy().hasHeightForWidth())
        self.DivBtn.setSizePolicy(sizePolicy)
        self.DivBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.DivBtn.setFont(font)
        self.DivBtn.setObjectName("DivBtn")
        self.gridLayout.addWidget(self.DivBtn, 8, 3, 1, 1)
        self.EulerBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EulerBtn.sizePolicy().hasHeightForWidth())
        self.EulerBtn.setSizePolicy(sizePolicy)
        self.EulerBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.EulerBtn.setFont(font)
        self.EulerBtn.setObjectName("EulerBtn")
        self.gridLayout.addWidget(self.EulerBtn, 5, 0, 1, 1)
        self.SixBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SixBtn.sizePolicy().hasHeightForWidth())
        self.SixBtn.setSizePolicy(sizePolicy)
        self.SixBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SixBtn.setFont(font)
        self.SixBtn.setObjectName("SixBtn")
        self.gridLayout.addWidget(self.SixBtn, 7, 2, 1, 1)
        self.RndBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RndBtn.sizePolicy().hasHeightForWidth())
        self.RndBtn.setSizePolicy(sizePolicy)
        self.RndBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.RndBtn.setFont(font)
        self.RndBtn.setObjectName("RndBtn")
        self.gridLayout.addWidget(self.RndBtn, 5, 2, 1, 1)
        self.RootBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RootBtn.sizePolicy().hasHeightForWidth())
        self.RootBtn.setSizePolicy(sizePolicy)
        self.RootBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.RootBtn.setFont(font)
        self.RootBtn.setObjectName("RootBtn")
        self.gridLayout.addWidget(self.RootBtn, 3, 1, 1, 1)
        self.DeusVult = QtWidgets.QPushButton(self.centralwidget)
        self.DeusVult.setMinimumSize(QtCore.QSize(80, 50))
        self.DeusVult.setMaximumSize(QtCore.QSize(80, 50))
        self.DeusVult.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DeusVult.setStyleSheet("border: 0px")
        self.DeusVult.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Cross_Templar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeusVult.setIcon(icon1)
        self.DeusVult.setIconSize(QtCore.QSize(42, 42))
        self.DeusVult.setObjectName("DeusVult")
        self.gridLayout.addWidget(self.DeusVult, 0, 0, 1, 1)
        self.NineBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NineBtn.sizePolicy().hasHeightForWidth())
        self.NineBtn.setSizePolicy(sizePolicy)
        self.NineBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.NineBtn.setFont(font)
        self.NineBtn.setObjectName("NineBtn")
        self.gridLayout.addWidget(self.NineBtn, 6, 2, 1, 1)
        self.EightBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EightBtn.sizePolicy().hasHeightForWidth())
        self.EightBtn.setSizePolicy(sizePolicy)
        self.EightBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.EightBtn.setFont(font)
        self.EightBtn.setObjectName("EightBtn")
        self.gridLayout.addWidget(self.EightBtn, 6, 1, 1, 1)
        self.TwoBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TwoBtn.sizePolicy().hasHeightForWidth())
        self.TwoBtn.setSizePolicy(sizePolicy)
        self.TwoBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TwoBtn.setFont(font)
        self.TwoBtn.setObjectName("TwoBtn")
        self.gridLayout.addWidget(self.TwoBtn, 8, 1, 1, 1)
        self.ThreeBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ThreeBtn.sizePolicy().hasHeightForWidth())
        self.ThreeBtn.setSizePolicy(sizePolicy)
        self.ThreeBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ThreeBtn.setFont(font)
        self.ThreeBtn.setObjectName("ThreeBtn")
        self.gridLayout.addWidget(self.ThreeBtn, 8, 2, 1, 1)
        self.FourBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FourBtn.sizePolicy().hasHeightForWidth())
        self.FourBtn.setSizePolicy(sizePolicy)
        self.FourBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.FourBtn.setFont(font)
        self.FourBtn.setObjectName("FourBtn")
        self.gridLayout.addWidget(self.FourBtn, 7, 0, 1, 1)
        self.DotBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DotBtn.sizePolicy().hasHeightForWidth())
        self.DotBtn.setSizePolicy(sizePolicy)
        self.DotBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.DotBtn.setFont(font)
        self.DotBtn.setObjectName("DotBtn")
        self.gridLayout.addWidget(self.DotBtn, 9, 1, 1, 1)
        self.AddBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddBtn.sizePolicy().hasHeightForWidth())
        self.AddBtn.setSizePolicy(sizePolicy)
        self.AddBtn.setMinimumSize(QtCore.QSize(80, 50))
        self.AddBtn.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.AddBtn.setFont(font)
        self.AddBtn.setObjectName("AddBtn")
        self.gridLayout.addWidget(self.AddBtn, 5, 3, 1, 1)
        self.AbsBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AbsBtn.sizePolicy().hasHeightForWidth())
        self.AbsBtn.setSizePolicy(sizePolicy)
        self.AbsBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AbsBtn.setFont(font)
        self.AbsBtn.setObjectName("AbsBtn")
        self.gridLayout.addWidget(self.AbsBtn, 4, 3, 1, 1)
        self.AnsBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnsBtn.sizePolicy().hasHeightForWidth())
        self.AnsBtn.setSizePolicy(sizePolicy)
        self.AnsBtn.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AnsBtn.setFont(font)
        self.AnsBtn.setObjectName("AnsBtn")
        self.gridLayout.addWidget(self.AnsBtn, 9, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionLicens = QtWidgets.QAction(MainWindow)
        self.actionLicens.setObjectName("actionLicens")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        self.CBtn.clicked.connect(self.Input.clear)
        self.Input.returnPressed.connect(self.EqualsBtn.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Input, self.CBtn)
        MainWindow.setTabOrder(self.CBtn, self.PowBtn)
        MainWindow.setTabOrder(self.PowBtn, self.RootBtn)
        MainWindow.setTabOrder(self.RootBtn, self.LogBtn)
        MainWindow.setTabOrder(self.LogBtn, self.BackspaceBtn)
        MainWindow.setTabOrder(self.BackspaceBtn, self.PercBtn)
        MainWindow.setTabOrder(self.PercBtn, self.PromBtn)
        MainWindow.setTabOrder(self.PromBtn, self.FactBtn)
        MainWindow.setTabOrder(self.FactBtn, self.AbsBtn)
        MainWindow.setTabOrder(self.AbsBtn, self.EulerBtn)
        MainWindow.setTabOrder(self.EulerBtn, self.PiBtn)
        MainWindow.setTabOrder(self.PiBtn, self.RndBtn)
        MainWindow.setTabOrder(self.RndBtn, self.AddBtn)
        MainWindow.setTabOrder(self.AddBtn, self.SevenBtn)
        MainWindow.setTabOrder(self.SevenBtn, self.EightBtn)
        MainWindow.setTabOrder(self.EightBtn, self.NineBtn)
        MainWindow.setTabOrder(self.NineBtn, self.SubBtn)
        MainWindow.setTabOrder(self.SubBtn, self.FourBtn)
        MainWindow.setTabOrder(self.FourBtn, self.FiveBtn)
        MainWindow.setTabOrder(self.FiveBtn, self.SixBtn)
        MainWindow.setTabOrder(self.SixBtn, self.MulBtn)
        MainWindow.setTabOrder(self.MulBtn, self.OneBtn)
        MainWindow.setTabOrder(self.OneBtn, self.TwoBtn)
        MainWindow.setTabOrder(self.TwoBtn, self.ThreeBtn)
        MainWindow.setTabOrder(self.ThreeBtn, self.DivBtn)
        MainWindow.setTabOrder(self.DivBtn, self.ZeroBtn)
        MainWindow.setTabOrder(self.ZeroBtn, self.DotBtn)
        MainWindow.setTabOrder(self.DotBtn, self.AnsBtn)
        MainWindow.setTabOrder(self.AnsBtn, self.EqualsBtn)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deus Vult Calculator"))
        self.SevenBtn.setText(_translate("MainWindow", "7"))
        self.SevenBtn.setShortcut(_translate("MainWindow", "7"))
        self.FactBtn.setText(_translate("MainWindow", "x!"))
        self.FactBtn.setShortcut(_translate("MainWindow", "!"))
        self.PiBtn.setText(_translate("MainWindow", "π"))
        self.OneBtn.setText(_translate("MainWindow", "1"))
        self.OneBtn.setShortcut(_translate("MainWindow", "1"))
        self.PowBtn.setText(_translate("MainWindow", "x^n"))
        self.BackspaceBtn.setText(_translate("MainWindow", "←"))
        self.BackspaceBtn.setShortcut(_translate("MainWindow", "Backspace"))
        self.PromBtn.setText(_translate("MainWindow", "‰"))
        self.MulBtn.setText(_translate("MainWindow", "×"))
        self.MulBtn.setShortcut(_translate("MainWindow", "*"))
        self.SubBtn.setText(_translate("MainWindow", "-"))
        self.SubBtn.setShortcut(_translate("MainWindow", "-"))
        self.FiveBtn.setText(_translate("MainWindow", "5"))
        self.FiveBtn.setShortcut(_translate("MainWindow", "5"))
        self.EqualsBtn.setText(_translate("MainWindow", "="))
        self.EqualsBtn.setShortcut(_translate("MainWindow", "Space"))
        self.PercBtn.setText(_translate("MainWindow", "%"))
        self.ZeroBtn.setText(_translate("MainWindow", "0"))
        self.ZeroBtn.setShortcut(_translate("MainWindow", "0"))
        self.CBtn.setText(_translate("MainWindow", "C"))
        self.CBtn.setShortcut(_translate("MainWindow", "Del"))
        self.LogBtn.setText(_translate("MainWindow", "log"))
        self.DivBtn.setText(_translate("MainWindow", "÷"))
        self.DivBtn.setShortcut(_translate("MainWindow", "/"))
        self.EulerBtn.setText(_translate("MainWindow", "e"))
        self.SixBtn.setText(_translate("MainWindow", "6"))
        self.SixBtn.setShortcut(_translate("MainWindow", "6"))
        self.RndBtn.setText(_translate("MainWindow", "Rnd"))
        self.RootBtn.setText(_translate("MainWindow", "√x"))
        self.NineBtn.setText(_translate("MainWindow", "9"))
        self.NineBtn.setShortcut(_translate("MainWindow", "9"))
        self.EightBtn.setText(_translate("MainWindow", "8"))
        self.EightBtn.setShortcut(_translate("MainWindow", "8"))
        self.TwoBtn.setText(_translate("MainWindow", "2"))
        self.TwoBtn.setShortcut(_translate("MainWindow", "2"))
        self.ThreeBtn.setText(_translate("MainWindow", "3"))
        self.ThreeBtn.setShortcut(_translate("MainWindow", "3"))
        self.FourBtn.setText(_translate("MainWindow", "4"))
        self.FourBtn.setShortcut(_translate("MainWindow", "4"))
        self.DotBtn.setText(_translate("MainWindow", "."))
        self.DotBtn.setShortcut(_translate("MainWindow", ","))
        self.AddBtn.setText(_translate("MainWindow", "+"))
        self.AddBtn.setShortcut(_translate("MainWindow", "+"))
        self.AbsBtn.setText(_translate("MainWindow", "abs"))
        self.AnsBtn.setText(_translate("MainWindow", "Ans"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionLicens.setText(_translate("MainWindow", "License"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


