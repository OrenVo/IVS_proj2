#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
import deus_calc

app = QApplication(sys.argv)

calc = deus_calc.Deus_Window()

sys.exit(app.exec_())
