import os
import re
import sys
import time
import Help as h
import random
import string
import pathlib
import datetime
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

#Version 0.3

class Variables():
    def __init__(self):
        self.generateLabelText = 'Generated in: '
        self.triesLabelText = 'Tries needed: '
        self._try = 1
        self.length = 8
        self.passMode = 'normal'
        self.safemode = False
        self.punctuation = string.punctuation
        self.final_password = 0
        self.weak = string.ascii_letters
        self.normal = string.ascii_letters + string.digits
        self.strong = string.ascii_letters + string.digits + string.punctuation
        self.custom = None

class Timers():
    def __init__(self):
        self.timer_start = None
        self.timer_time = None

class passgenUI(object):
    def setupUi(self, passwordUI):
        passwordUI.setObjectName("passwordUI")
        passwordUI.resize(551, 253)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(passwordUI.sizePolicy().hasHeightForWidth())
        passwordUI.setSizePolicy(sizePolicy)
        passwordUI.setMinimumSize(QtCore.QSize(551, 253))
        passwordUI.setMaximumSize(QtCore.QSize(551, 253))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(31, 35, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        passwordUI.setPalette(palette)
        self.generateButton = QtWidgets.QPushButton(passwordUI)
        self.generateButton.setGeometry(QtCore.QRect(420, 92, 91, 31))
        self.generateButton.setObjectName("generateButton")
        self.generateButton.clicked.connect(self.generatePassword)
        self.passwordBox = QtWidgets.QLineEdit(passwordUI)
        self.passwordBox.setGeometry(QtCore.QRect(110, 90, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordBox.setFont(font)
        self.passwordBox.setObjectName("passwordBox")
        self.passwordBox.textChanged.connect(self.checkCopyButtonAvailability)
        self.copyButton = QtWidgets.QPushButton(passwordUI)
        self.copyButton.setGeometry(QtCore.QRect(420, 130, 91, 31))
        self.copyButton.setObjectName("copyButton")
        self.copyButton.clicked.connect(self.copyToClipBoard)
        self.copyButton.setEnabled(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(passwordUI)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 128, 371, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.modeHorizLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.modeHorizLayout.setContentsMargins(0, 0, 0, 0)
        self.modeHorizLayout.setObjectName("modeHorizLayout")
        self.weakRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.weakRadioButton.setObjectName("weakRadioButton")
        self.weakRadioButton.clicked.connect(self.modeCheck)
        self.modeHorizLayout.addWidget(self.weakRadioButton)
        self.normalRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.normalRadioButton.setChecked(True)
        self.normalRadioButton.setObjectName("normalRadioButton")
        self.normalRadioButton.clicked.connect(self.modeCheck)
        self.modeHorizLayout.addWidget(self.normalRadioButton)
        self.strongRadioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.strongRadioButton.setObjectName("strongRadioButton")
        self.strongRadioButton.clicked.connect(self.modeCheck)
        self.modeHorizLayout.addWidget(self.strongRadioButton)
        self.safemodeCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.safemodeCheckBox.setObjectName("safemodeCheckBox")
        self.safemodeCheckBox.stateChanged.connect(self.checkSafemode)
        self.modeHorizLayout.addWidget(self.safemodeCheckBox)
        self.languageButton = QtWidgets.QPushButton(passwordUI)
        self.languageButton.setGeometry(QtCore.QRect(510, 10, 31, 31))
        self.languageButton.setObjectName("languageButton")
        self.languageButton.hide()
        self.timeLabel = QtWidgets.QLabel(passwordUI)
        self.timeLabel.setGeometry(QtCore.QRect(10, 220, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.triesLabel = QtWidgets.QLabel(passwordUI)
        self.triesLabel.setGeometry(QtCore.QRect(220, 220, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.triesLabel.setFont(font)
        self.triesLabel.setObjectName("triesLabel")
        self.aboutButton = QtWidgets.QPushButton(passwordUI)
        self.aboutButton.setGeometry(QtCore.QRect(480, 220, 61, 25))
        self.aboutButton.setObjectName("aboutButton")
        self.aboutButton.clicked.connect(self.showDialog)
        self.passLengthBox = QtWidgets.QSpinBox(passwordUI)
        self.passLengthBox.setGeometry(QtCore.QRect(40, 90, 61, 31))
        self.passLengthBox.setMinimum(1)
        self.passLengthBox.setMaximum(10000000)
        self.passLengthBox.setProperty("value", 8)
        self.passLengthBox.setObjectName("passLengthBox")
        self.passLengthBox.textChanged.connect(self.checkLength)
        self.helpButton = QtWidgets.QPushButton(passwordUI)
        self.helpButton.setGeometry(QtCore.QRect(408, 220, 61, 25))
        self.helpButton.setObjectName("helpButton")
        self.helpButton.clicked.connect(self.showHelp)

        self.retranslateUi(passwordUI)
        QtCore.QMetaObject.connectSlotsByName(passwordUI)

    def retranslateUi(self, passwordUI):
        _translate = QtCore.QCoreApplication.translate
        passwordUI.setWindowTitle(_translate("passwordUI", "Passgen.py"))
        self.generateButton.setText(_translate("passwordUI", "Generate"))
        self.copyButton.setText(_translate("passwordUI", "Copy"))
        self.weakRadioButton.setText(_translate("passwordUI", "Weak"))
        self.normalRadioButton.setText(_translate("passwordUI", "Normal"))
        self.strongRadioButton.setText(_translate("passwordUI", "Strong"))
        self.safemodeCheckBox.setText(_translate("passwordUI", "Safemode"))
        self.languageButton.setText(_translate("passwordUI", "En"))
        self.timeLabel.setText(_translate("passwordUI", "Generated in: "))
        self.triesLabel.setText(_translate("passwordUI", "Tries needed: "))
        self.aboutButton.setText(_translate("passwordUI", "About"))
        self.helpButton.setText(_translate("passwordUI", "Help"))

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Programmed by github.com/itsthooor\nProject Github -> https://github.com/itsthooor/passgen\nProject Passgen is licensed under GNU General Public License v2.0")
        msgBox.setWindowTitle("About Passgen.py")
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def showHelp(self):
        app = QtWidgets.QApplication(sys.argv)
        help = QtWidgets.QWidget()
        ui = h.helpUI()
        ui.getImagePath = str(pathlib.Path(__file__).parent.absolute()) + '/bin/Help.jpg'
        ui.setupUi(help)
        help.show()
        help.showUI()
        sys.exit(app.exec_())

    def modeCheck(self):
        if self.weakRadioButton.isChecked():
            variables.passMode = 'weak'
            self.safemodeCheckBox.setChecked(False)
            self.safemodeCheckBox.setEnabled(False)
        elif self.normalRadioButton.isChecked():
            variables.passMode = 'normal'
            self.safemodeCheckBox.setEnabled(True)
        elif self.strongRadioButton.isChecked():
            variables.passMode = 'strong'
            self.safemodeCheckBox.setEnabled(True)

    def checkLength(self):
        variables.length = self.passLengthBox.value()
        print(variables.length)

    def checkSafemode(self):
        if self.safemodeCheckBox.isChecked():
            variables.safemode = True
        else:
            variables.safemode = False
        print('Safemode:',variables.safemode)

    def checkCopyButtonAvailability(self):
        if self.passwordBox.text in (None, ''):
            self.copyButton.setEnabled(False)
        else:
            self.copyButton.setEnabled(True)

    def copyToClipBoard(self):
        pyperclip.copy(variables.final_password)
        clipped = pyperclip.paste()
        print(clipped)
        copyBox = QMessageBox()
        copyBox.setIcon(QMessageBox.Information)
        copyBox.setText("Copied successfully!")
        copyBox.setWindowTitle("Info")
        copyBox.setStandardButtons(QMessageBox.Ok)

        returnValue = copyBox.exec()
        if returnValue == QMessageBox.Ok:
            print('Closed')

    def printTries(self, _try):
        if _try == 0:
            self.triesLabel.setText(variables.triesLabelText)
        else:
            self.triesLabel.setText(variables.triesLabelText + str(_try))

    def generatePassword(self):
        generate()
        self.timeLabel.setText(variables.generateLabelText+timer1.timer_time)
        self.passwordBox.setText(variables.final_password)

ui = passgenUI()
variables = Variables()
timer1 = Timers()

def tries(silent=False):
    variables._try += 1
    if not silent:
        print('Try nr.:',variables._try)
        ui.printTries(variables._try)

def timer_st():
    timer1.timer_start = time.perf_counter()

def timer_stop():
    timer_gen_end = time.perf_counter()
    timer_gen_eq = timer_gen_end - timer1.timer_start
    timer1.timer_time = str(datetime.timedelta(seconds=round(timer_gen_eq)))

def charsSelected(mode):
    selMode = None
    if mode == 'weak':
        selMode = variables.weak
    elif mode == 'normal':
        selMode = variables.normal
    else:
        selMode = variables.strong
    return selMode


def generate():
    variables._try = 1
    ui.printTries(0)
    mode = variables.passMode
    chars = charsSelected(mode)
    length = variables.length
    safemode = variables.safemode
    timer_st()
    if safemode == True:
        print('Safemode activated!')
        print(mode)
        password = ''.join(random.choice(chars) for x in range(length))
        if mode == 'normal':
            intgen = re.findall(r'\d+', str(password))
            while len(intgen) < (length / 2):
                tries()
                password = ''.join(random.choice(chars) for x in range(length))
                intgen = re.findall(r'\d+', str(password))
        if mode == 'strong':
            print('Mode working')
            lettergenerator = re.findall("[A-Z]+", str(password))
            intgen = re.findall(r'\d+', str(password))
            while len(lettergenerator) < (length / 5):
                print(1)
                tries()
                password = ''.join(random.choice(chars) for x in range(length))
                lettergenerator = re.findall("[A-Z]+", str(password))
            while len(lettergenerator) > (length / 4):
                print(2)
                tries()
                password = ''.join(random.choice(chars) for x in range(length))
                lettergenerator = re.findall("[A-Z]+", str(password))
            while len(intgen) < (length / 5):
                print(3)
                tries()
                password = ''.join(random.choice(chars) for x in range(length))
                intgen = re.findall(r'\d+', str(password))
            while len(intgen) > (length / 4):
                print(4)
                tries()
                password = ''.join(random.choice(chars) for x in range(length))
                intgen = re.findall(r'\d+', str(password))
        variables.final_password = password
    else:
        password = ''.join(random.choice(chars) for x in range(length))
        variables.final_password = password
        ui.printTries(1)
    timer_stop()
    variables._try = 1
    #print(variables.final_password)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    passwordUI = QtWidgets.QWidget()
    ui = passgenUI()
    ui.setupUi(passwordUI)
    passwordUI.show()
    sys.exit(app.exec_())
