# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sucesso.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(355, 135)
        self.labelTitulo = QtWidgets.QLabel(Form)
        self.labelTitulo.setGeometry(QtCore.QRect(0, 20, 351, 20))
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelMensagem = QtWidgets.QLabel(Form)
        self.labelMensagem.setGeometry(QtCore.QRect(0, 40, 351, 41))
        self.labelMensagem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMensagem.setObjectName("labelMensagem")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 80, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitulo.setText(_translate("Form", "TextLabel"))
        self.labelMensagem.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "Ok"))

