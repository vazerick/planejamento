# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 618)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeItens = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeItens.setGeometry(QtCore.QRect(60, 266, 391, 301))
        self.treeItens.setStyleSheet("")
        self.treeItens.setDragEnabled(True)
        self.treeItens.setAlternatingRowColors(True)
        self.treeItens.setObjectName("treeItens")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeItens)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.treeItens.header().setVisible(False)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 16, 341, 191))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageInstrucoes = QtWidgets.QWidget()
        self.pageInstrucoes.setObjectName("pageInstrucoes")
        self.labelInstrucoes = QtWidgets.QLabel(self.pageInstrucoes)
        self.labelInstrucoes.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.labelInstrucoes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelInstrucoes.setObjectName("labelInstrucoes")
        self.stackedWidget.addWidget(self.pageInstrucoes)
        self.pageAdd = QtWidgets.QWidget()
        self.pageAdd.setObjectName("pageAdd")
        self.label_6 = QtWidgets.QLabel(self.pageAdd)
        self.label_6.setGeometry(QtCore.QRect(260, 10, 71, 17))
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.pageAdd)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.pageAdd)
        self.label_12.setGeometry(QtCore.QRect(160, 10, 54, 17))
        self.label_12.setObjectName("label_12")
        self.lineAddNome = QtWidgets.QLineEdit(self.pageAdd)
        self.lineAddNome.setGeometry(QtCore.QRect(20, 30, 131, 25))
        self.lineAddNome.setObjectName("lineAddNome")
        self.spinAddPrioridade = QtWidgets.QSpinBox(self.pageAdd)
        self.spinAddPrioridade.setGeometry(QtCore.QRect(270, 90, 51, 26))
        self.spinAddPrioridade.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinAddPrioridade.setObjectName("spinAddPrioridade")
        self.label_13 = QtWidgets.QLabel(self.pageAdd)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.label_13.setObjectName("label_13")
        self.textAddComentarios = QtWidgets.QTextEdit(self.pageAdd)
        self.textAddComentarios.setGeometry(QtCore.QRect(20, 80, 221, 61))
        self.textAddComentarios.setObjectName("textAddComentarios")
        self.spinAddPreco = QtWidgets.QDoubleSpinBox(self.pageAdd)
        self.spinAddPreco.setGeometry(QtCore.QRect(170, 30, 81, 26))
        self.spinAddPreco.setMaximum(9999.99)
        self.spinAddPreco.setObjectName("spinAddPreco")
        self.label_14 = QtWidgets.QLabel(self.pageAdd)
        self.label_14.setGeometry(QtCore.QRect(260, 70, 61, 17))
        self.label_14.setObjectName("label_14")
        self.spinAddPrestacoes = QtWidgets.QSpinBox(self.pageAdd)
        self.spinAddPrestacoes.setGeometry(QtCore.QRect(270, 30, 51, 26))
        self.spinAddPrestacoes.setObjectName("spinAddPrestacoes")
        self.buttonAddAdicionar = QtWidgets.QPushButton(self.pageAdd)
        self.buttonAddAdicionar.setGeometry(QtCore.QRect(240, 150, 80, 25))
        self.buttonAddAdicionar.setObjectName("buttonAddAdicionar")
        self.buttonCancelar = QtWidgets.QPushButton(self.pageAdd)
        self.buttonCancelar.setGeometry(QtCore.QRect(130, 150, 80, 25))
        self.buttonCancelar.setObjectName("buttonCancelar")
        self.stackedWidget.addWidget(self.pageAdd)
        self.pageEdit = QtWidgets.QWidget()
        self.pageEdit.setObjectName("pageEdit")
        self.label = QtWidgets.QLabel(self.pageEdit)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 17))
        self.label.setObjectName("label")
        self.lineNome = QtWidgets.QLineEdit(self.pageEdit)
        self.lineNome.setGeometry(QtCore.QRect(20, 30, 131, 25))
        self.lineNome.setObjectName("lineNome")
        self.label_2 = QtWidgets.QLabel(self.pageEdit)
        self.label_2.setGeometry(QtCore.QRect(160, 10, 54, 17))
        self.label_2.setObjectName("label_2")
        self.spinPreco = QtWidgets.QDoubleSpinBox(self.pageEdit)
        self.spinPreco.setGeometry(QtCore.QRect(170, 30, 81, 26))
        self.spinPreco.setMaximum(9999.99)
        self.spinPreco.setObjectName("spinPreco")
        self.label_3 = QtWidgets.QLabel(self.pageEdit)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 71, 17))
        self.label_3.setObjectName("label_3")
        self.spinPrestacoes = QtWidgets.QSpinBox(self.pageEdit)
        self.spinPrestacoes.setGeometry(QtCore.QRect(270, 30, 51, 26))
        self.spinPrestacoes.setObjectName("spinPrestacoes")
        self.textComentarios = QtWidgets.QTextEdit(self.pageEdit)
        self.textComentarios.setGeometry(QtCore.QRect(20, 80, 221, 61))
        self.textComentarios.setObjectName("textComentarios")
        self.label_4 = QtWidgets.QLabel(self.pageEdit)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 71, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.pageEdit)
        self.label_5.setGeometry(QtCore.QRect(260, 70, 61, 17))
        self.label_5.setObjectName("label_5")
        self.spinPrioridade = QtWidgets.QSpinBox(self.pageEdit)
        self.spinPrioridade.setGeometry(QtCore.QRect(270, 90, 51, 26))
        self.spinPrioridade.setObjectName("spinPrioridade")
        self.buttonExcluir = QtWidgets.QPushButton(self.pageEdit)
        self.buttonExcluir.setGeometry(QtCore.QRect(20, 150, 80, 25))
        self.buttonExcluir.setObjectName("buttonExcluir")
        self.buttonSalvar = QtWidgets.QPushButton(self.pageEdit)
        self.buttonSalvar.setGeometry(QtCore.QRect(240, 150, 80, 25))
        self.buttonSalvar.setObjectName("buttonSalvar")
        self.buttonDesfazer = QtWidgets.QPushButton(self.pageEdit)
        self.buttonDesfazer.setGeometry(QtCore.QRect(130, 150, 80, 25))
        self.buttonDesfazer.setObjectName("buttonDesfazer")
        self.stackedWidget.addWidget(self.pageEdit)
        self.pagePrioridade = QtWidgets.QWidget()
        self.pagePrioridade.setObjectName("pagePrioridade")
        self.label_8 = QtWidgets.QLabel(self.pagePrioridade)
        self.label_8.setGeometry(QtCore.QRect(250, 60, 54, 17))
        self.label_8.setObjectName("label_8")
        self.spinEspera = QtWidgets.QSpinBox(self.pagePrioridade)
        self.spinEspera.setGeometry(QtCore.QRect(260, 80, 51, 26))
        self.spinEspera.setObjectName("spinEspera")
        self.label_10 = QtWidgets.QLabel(self.pagePrioridade)
        self.label_10.setGeometry(QtCore.QRect(250, 20, 61, 17))
        self.label_10.setObjectName("label_10")
        self.labelPrioridade = QtWidgets.QLabel(self.pagePrioridade)
        self.labelPrioridade.setGeometry(QtCore.QRect(260, 40, 54, 17))
        self.labelPrioridade.setObjectName("labelPrioridade")
        self.listItens = QtWidgets.QTreeWidget(self.pagePrioridade)
        self.listItens.setGeometry(QtCore.QRect(10, 10, 231, 171))
        self.listItens.setLineWidth(0)
        self.listItens.setAlternatingRowColors(False)
        self.listItens.setRootIsDecorated(False)
        self.listItens.setItemsExpandable(False)
        self.listItens.setObjectName("listItens")
        self.listItens.header().setVisible(False)
        self.buttonPrioridadeSalvar = QtWidgets.QPushButton(self.pagePrioridade)
        self.buttonPrioridadeSalvar.setGeometry(QtCore.QRect(250, 150, 80, 25))
        self.buttonPrioridadeSalvar.setObjectName("buttonPrioridadeSalvar")
        self.buttonPrioridadeRetornar = QtWidgets.QPushButton(self.pagePrioridade)
        self.buttonPrioridadeRetornar.setGeometry(QtCore.QRect(250, 120, 80, 25))
        self.buttonPrioridadeRetornar.setObjectName("buttonPrioridadeRetornar")
        self.stackedWidget.addWidget(self.pagePrioridade)
        self.buttonAdicionar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdicionar.setGeometry(QtCore.QRect(50, 226, 80, 31))
        self.buttonAdicionar.setObjectName("buttonAdicionar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 26, 71, 17))
        self.label_7.setObjectName("label_7")
        self.comboMes = QtWidgets.QComboBox(self.centralwidget)
        self.comboMes.setGeometry(QtCore.QRect(520, 46, 91, 25))
        self.comboMes.setStyleSheet("")
        self.comboMes.setObjectName("comboMes")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.comboMes.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 26, 54, 17))
        self.label_9.setObjectName("label_9")
        self.spinLimite = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinLimite.setGeometry(QtCore.QRect(630, 46, 91, 26))
        self.spinLimite.setMaximum(9999.99)
        self.spinLimite.setObjectName("spinLimite")
        self.treeResultado = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeResultado.setGeometry(QtCore.QRect(500, 86, 381, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeResultado.sizePolicy().hasHeightForWidth())
        self.treeResultado.setSizePolicy(sizePolicy)
        self.treeResultado.setSizeIncrement(QtCore.QSize(0, 0))
        self.treeResultado.setLineWidth(1)
        self.treeResultado.setMidLineWidth(0)
        self.treeResultado.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeResultado.setProperty("showDropIndicator", True)
        self.treeResultado.setAlternatingRowColors(True)
        self.treeResultado.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeResultado.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeResultado.setTextElideMode(QtCore.Qt.ElideNone)
        self.treeResultado.setIndentation(20)
        self.treeResultado.setRootIsDecorated(True)
        self.treeResultado.setUniformRowHeights(False)
        self.treeResultado.setAllColumnsShowFocus(False)
        self.treeResultado.setWordWrap(False)
        self.treeResultado.setObjectName("treeResultado")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeResultado)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.treeResultado.header().setVisible(False)
        self.treeResultado.header().setCascadingSectionResizes(False)
        self.treeResultado.header().setDefaultSectionSize(75)
        self.treeResultado.header().setMinimumSectionSize(75)
        self.treeResultado.header().setStretchLastSection(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 206, 301, 51))
        self.groupBox.setObjectName("groupBox")
        self.buttonTempo = QtWidgets.QPushButton(self.groupBox)
        self.buttonTempo.setGeometry(QtCore.QRect(40, 24, 91, 21))
        self.buttonTempo.setObjectName("buttonTempo")
        self.buttonTempoPrioridade = QtWidgets.QPushButton(self.groupBox)
        self.buttonTempoPrioridade.setGeometry(QtCore.QRect(170, 24, 91, 21))
        self.buttonTempoPrioridade.setObjectName("buttonTempoPrioridade")
        self.buttonGrafico = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGrafico.setGeometry(QtCore.QRect(810, 46, 61, 25))
        self.buttonGrafico.setObjectName("buttonGrafico")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineNome, self.spinPreco)
        MainWindow.setTabOrder(self.spinPreco, self.spinPrestacoes)
        MainWindow.setTabOrder(self.spinPrestacoes, self.spinPrioridade)
        MainWindow.setTabOrder(self.spinPrioridade, self.textComentarios)
        MainWindow.setTabOrder(self.textComentarios, self.buttonSalvar)
        MainWindow.setTabOrder(self.buttonSalvar, self.lineAddNome)
        MainWindow.setTabOrder(self.lineAddNome, self.spinAddPreco)
        MainWindow.setTabOrder(self.spinAddPreco, self.spinAddPrestacoes)
        MainWindow.setTabOrder(self.spinAddPrestacoes, self.spinAddPrioridade)
        MainWindow.setTabOrder(self.spinAddPrioridade, self.buttonAddAdicionar)
        MainWindow.setTabOrder(self.buttonAddAdicionar, self.buttonCancelar)
        MainWindow.setTabOrder(self.buttonCancelar, self.textAddComentarios)
        MainWindow.setTabOrder(self.textAddComentarios, self.buttonExcluir)
        MainWindow.setTabOrder(self.buttonExcluir, self.treeItens)
        MainWindow.setTabOrder(self.treeItens, self.buttonDesfazer)
        MainWindow.setTabOrder(self.buttonDesfazer, self.spinEspera)
        MainWindow.setTabOrder(self.spinEspera, self.buttonPrioridadeSalvar)
        MainWindow.setTabOrder(self.buttonPrioridadeSalvar, self.buttonPrioridadeRetornar)
        MainWindow.setTabOrder(self.buttonPrioridadeRetornar, self.buttonAdicionar)
        MainWindow.setTabOrder(self.buttonAdicionar, self.comboMes)
        MainWindow.setTabOrder(self.comboMes, self.spinLimite)
        MainWindow.setTabOrder(self.spinLimite, self.treeResultado)
        MainWindow.setTabOrder(self.treeResultado, self.listItens)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Planejamento"))
        self.treeItens.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeItens.headerItem().setText(1, _translate("MainWindow", "2"))
        self.treeItens.headerItem().setText(2, _translate("MainWindow", "3"))
        __sortingEnabled = self.treeItens.isSortingEnabled()
        self.treeItens.setSortingEnabled(False)
        self.treeItens.topLevelItem(0).setText(0, _translate("MainWindow", "Prioridade 1"))
        self.treeItens.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Item"))
        self.treeItens.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "R$10,00"))
        self.treeItens.topLevelItem(0).child(0).setText(2, _translate("MainWindow", "4x"))
        self.treeItens.setSortingEnabled(__sortingEnabled)
        self.labelInstrucoes.setText(_translate("MainWindow", "Instruções:"))
        self.label_6.setText(_translate("MainWindow", "Prestações:"))
        self.label_11.setText(_translate("MainWindow", "Comentários"))
        self.label_12.setText(_translate("MainWindow", "Preço:"))
        self.label_13.setText(_translate("MainWindow", "Nome:"))
        self.textAddComentarios.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Prioridade:"))
        self.buttonAddAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.buttonCancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Preço:"))
        self.label_3.setText(_translate("MainWindow", "Prestações:"))
        self.textComentarios.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Comentários"))
        self.label_5.setText(_translate("MainWindow", "Prioridade:"))
        self.buttonExcluir.setText(_translate("MainWindow", "Excluir"))
        self.buttonSalvar.setText(_translate("MainWindow", "Salvar"))
        self.buttonDesfazer.setText(_translate("MainWindow", "Desfazer"))
        self.label_8.setText(_translate("MainWindow", "Espera:"))
        self.label_10.setText(_translate("MainWindow", "Prioridade:"))
        self.labelPrioridade.setText(_translate("MainWindow", "1"))
        self.listItens.headerItem().setText(0, _translate("MainWindow", "A"))
        self.listItens.headerItem().setText(1, _translate("MainWindow", "B"))
        self.buttonPrioridadeSalvar.setText(_translate("MainWindow", "Salvar"))
        self.buttonPrioridadeRetornar.setText(_translate("MainWindow", "Desfazer"))
        self.buttonAdicionar.setText(_translate("MainWindow", "Adicionar"))
        self.label_7.setText(_translate("MainWindow", "Mês inicial:"))
        self.comboMes.setItemText(0, _translate("MainWindow", "Janeiro"))
        self.comboMes.setItemText(1, _translate("MainWindow", "Fevereiro"))
        self.comboMes.setItemText(2, _translate("MainWindow", "Março"))
        self.comboMes.setItemText(3, _translate("MainWindow", "Abril"))
        self.comboMes.setItemText(4, _translate("MainWindow", "Maio"))
        self.comboMes.setItemText(5, _translate("MainWindow", "Junho"))
        self.comboMes.setItemText(6, _translate("MainWindow", "Julho"))
        self.comboMes.setItemText(7, _translate("MainWindow", "Agosto"))
        self.comboMes.setItemText(8, _translate("MainWindow", "Setembro"))
        self.comboMes.setItemText(9, _translate("MainWindow", "Outubro"))
        self.comboMes.setItemText(10, _translate("MainWindow", "Novembro"))
        self.comboMes.setItemText(11, _translate("MainWindow", "Dezembro"))
        self.label_9.setText(_translate("MainWindow", "Limite:"))
        self.treeResultado.headerItem().setText(0, _translate("MainWindow", "1"))
        self.treeResultado.headerItem().setText(1, _translate("MainWindow", "2"))
        self.treeResultado.headerItem().setText(2, _translate("MainWindow", "3"))
        __sortingEnabled = self.treeResultado.isSortingEnabled()
        self.treeResultado.setSortingEnabled(False)
        self.treeResultado.topLevelItem(0).setText(0, _translate("MainWindow", "Maio"))
        self.treeResultado.topLevelItem(0).setText(1, _translate("MainWindow", "R$100,00"))
        self.treeResultado.topLevelItem(0).setText(2, _translate("MainWindow", "50%"))
        self.treeResultado.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Prioridade 1"))
        self.treeResultado.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "R$100,00"))
        self.treeResultado.topLevelItem(0).child(0).child(0).setText(0, _translate("MainWindow", "Item"))
        self.treeResultado.topLevelItem(0).child(0).child(0).setText(1, _translate("MainWindow", "R$10,00"))
        self.treeResultado.topLevelItem(0).child(0).child(0).setText(2, _translate("MainWindow", "1/5"))
        self.treeResultado.topLevelItem(0).child(0).child(1).setText(0, _translate("MainWindow", "Item2"))
        self.treeResultado.topLevelItem(0).child(0).child(1).setText(1, _translate("MainWindow", "R$90,00"))
        self.treeResultado.topLevelItem(0).child(0).child(1).setText(2, _translate("MainWindow", "1/1"))
        self.treeResultado.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "Passar o mês"))
        self.buttonTempo.setText(_translate("MainWindow", "Prestação"))
        self.buttonTempoPrioridade.setText(_translate("MainWindow", "Prioridade"))
        self.buttonGrafico.setText(_translate("MainWindow", "Gráfico"))

