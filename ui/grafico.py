# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafico.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(862, 688)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(390, 650, 80, 25))
        self.pushButton.setObjectName("pushButton")
        self.widget = PlotCanvas(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 841, 601))
        self.widget.setObjectName("widget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gráfico"))
        self.pushButton.setText(_translate("Form", "Ok"))

from ui.plotcanvas import PlotCanvas
