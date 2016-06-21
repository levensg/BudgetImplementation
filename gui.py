# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(710, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-30, -10, 791, 551))
        self.frame.setMouseTracking(True)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.TYPE_te = QtGui.QLineEdit(self.frame)
        self.TYPE_te.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.TYPE_te.setObjectName(_fromUtf8("TYPE_te"))
        self.AMOUNT_te = QtGui.QLineEdit(self.frame)
        self.AMOUNT_te.setGeometry(QtCore.QRect(240, 50, 113, 20))
        self.AMOUNT_te.setObjectName(_fromUtf8("AMOUNT_te"))
        self.DESCRIPTION_te = QtGui.QLineEdit(self.frame)
        self.DESCRIPTION_te.setGeometry(QtCore.QRect(370, 50, 113, 20))
        self.DESCRIPTION_te.setObjectName(_fromUtf8("DESCRIPTION_te"))
        self.BALANCE_te = QtGui.QLineEdit(self.frame)
        self.BALANCE_te.setGeometry(QtCore.QRect(280, 130, 113, 20))
        self.BALANCE_te.setObjectName(_fromUtf8("BALANCE_te"))
        self.ADD_btn = QtGui.QPushButton(self.frame)
        self.ADD_btn.setGeometry(QtCore.QRect(110, 200, 75, 23))
        self.ADD_btn.setObjectName(_fromUtf8("ADD_btn"))
        self.EXIT_btn = QtGui.QPushButton(self.frame)
        self.EXIT_btn.setGeometry(QtCore.QRect(490, 200, 75, 23))
        self.EXIT_btn.setObjectName(_fromUtf8("EXIT_btn"))
        self.REMOVE_btn = QtGui.QPushButton(self.frame)
        self.REMOVE_btn.setGeometry(QtCore.QRect(240, 200, 75, 23))
        self.REMOVE_btn.setObjectName(_fromUtf8("REMOVE_btn"))
        self.BALANCE_btn = QtGui.QPushButton(self.frame)
        self.BALANCE_btn.setGeometry(QtCore.QRect(440, 130, 75, 23))
        self.BALANCE_btn.setObjectName(_fromUtf8("BALANCE_btn"))
        self.REPORT_ALL_btn = QtGui.QPushButton(self.frame)
        self.REPORT_ALL_btn.setGeometry(QtCore.QRect(360, 200, 75, 23))
        self.REPORT_ALL_btn.setObjectName(_fromUtf8("REPORT_ALL_btn"))
        self.REPORT_lbl = QtGui.QLabel(self.frame)
        self.REPORT_lbl.setGeometry(QtCore.QRect(110, 280, 451, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.REPORT_lbl.setFont(font)
        self.REPORT_lbl.setText(_fromUtf8(""))
        self.REPORT_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.REPORT_lbl.setObjectName(_fromUtf8("REPORT_lbl"))
        self.TYPE_lbl = QtGui.QLabel(self.frame)
        self.TYPE_lbl.setGeometry(QtCore.QRect(150, 30, 46, 13))
        self.TYPE_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.TYPE_lbl.setObjectName(_fromUtf8("TYPE_lbl"))
        self.AMOUNT_lbl = QtGui.QLabel(self.frame)
        self.AMOUNT_lbl.setGeometry(QtCore.QRect(270, 30, 46, 13))
        self.AMOUNT_lbl.setObjectName(_fromUtf8("AMOUNT_lbl"))
        self.DESCRIPTIONLbl = QtGui.QLabel(self.frame)
        self.DESCRIPTIONLbl.setGeometry(QtCore.QRect(400, 30, 61, 16))
        self.DESCRIPTIONLbl.setObjectName(_fromUtf8("DESCRIPTIONLbl"))
        self.IN_OUT_lbl = QtGui.QLabel(self.frame)
        self.IN_OUT_lbl.setGeometry(QtCore.QRect(510, 30, 46, 13))
        self.IN_OUT_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.IN_OUT_lbl.setObjectName(_fromUtf8("IN_OUT_lbl"))
        self.IN_OUT_cb = QtGui.QComboBox(self.frame)
        self.IN_OUT_cb.setEnabled(True)
        self.IN_OUT_cb.setGeometry(QtCore.QRect(500, 50, 69, 22))
        self.IN_OUT_cb.setMouseTracking(True)
        self.IN_OUT_cb.setObjectName(_fromUtf8("IN_OUT_cb"))
        self.IN_OUT_cb.addItem(_fromUtf8(""))
        self.IN_OUT_cb.addItem(_fromUtf8(""))
        self.BALANCE_lbl = QtGui.QLabel(self.frame)
        self.BALANCE_lbl.setGeometry(QtCore.QRect(310, 100, 46, 16))
        self.BALANCE_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.BALANCE_lbl.setObjectName(_fromUtf8("BALANCE_lbl"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ADD_btn.setText(_translate("MainWindow", "ADD", None))
        self.EXIT_btn.setText(_translate("MainWindow", "EXIT", None))
        self.REMOVE_btn.setText(_translate("MainWindow", "REMOVE", None))
        self.BALANCE_btn.setText(_translate("MainWindow", "BALANCE", None))
        self.REPORT_ALL_btn.setText(_translate("MainWindow", "REPORT ALL", None))
        self.TYPE_lbl.setText(_translate("MainWindow", "Type", None))
        self.AMOUNT_lbl.setText(_translate("MainWindow", "Amount", None))
        self.DESCRIPTIONLbl.setText(_translate("MainWindow", "Description", None))
        self.IN_OUT_lbl.setText(_translate("MainWindow", "IN/OUT", None))
        self.IN_OUT_cb.setItemText(0, _translate("MainWindow", "IN", None))
        self.IN_OUT_cb.setItemText(1, _translate("MainWindow", "OUT", None))
        self.BALANCE_lbl.setText(_translate("MainWindow", "Balance", None))

