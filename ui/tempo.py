# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tempo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 445)
        self.labelTitulo = QtWidgets.QLabel(Form)
        self.labelTitulo.setGeometry(QtCore.QRect(80, 20, 351, 20))
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelMensagem = QtWidgets.QLabel(Form)
        self.labelMensagem.setGeometry(QtCore.QRect(80, 40, 351, 41))
        self.labelMensagem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMensagem.setObjectName("labelMensagem")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 410, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.listItens = QtWidgets.QTreeWidget(Form)
        self.listItens.setGeometry(QtCore.QRect(20, 80, 481, 311))
        self.listItens.setLineWidth(0)
        self.listItens.setProperty("showDropIndicator", True)
        self.listItens.setAlternatingRowColors(True)
        self.listItens.setRootIsDecorated(True)
        self.listItens.setItemsExpandable(True)
        self.listItens.setObjectName("listItens")
        self.listItens.header().setVisible(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Passar Tempo"))
        self.labelTitulo.setText(_translate("Form", "TextLabel"))
        self.labelMensagem.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "Ok"))
        self.listItens.headerItem().setText(0, _translate("Form", "a"))
        self.listItens.headerItem().setText(1, _translate("Form", "New Column"))
        self.listItens.headerItem().setText(2, _translate("Form", "a"))

