import sys
import sass

# import do PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QDate

# import das janelas

from ui.main import Ui_MainWindow as Main
from ui.excluir import Ui_Form as Excluir
from ui.sucesso import Ui_Form as Ok

class gui:

    def __init__(self):
# declarações da interface gráfica

        self.app = QApplication(sys.argv)

# janela principal
        self.wMain = QMainWindow()
        self.ui = Main()
        self.ui.setupUi(self.wMain)

        self.ui.treeItens.setColumnWidth(0, 175)
        self.ui.treeResultado.setColumnWidth(0, 200)

        self.wExcluir = QDialog()
        self.uiExcluir = Excluir()
        self.uiExcluir.setupUi(self.wExcluir)

        self.wOk = QDialog()
        self.uiOk = Ok()
        self.uiOk.setupUi(self.wOk)


# seta a mesma folha de estilos e bloqueio para todas as janelas


        tema = sass.compile(filename="ui/style.scss")


        self.wMain.setStyleSheet(tema)
        self.wMain.show()


        for janela in [
            self.wMain,
            self.wExcluir,
            self.wOk
        ]:
            janela.setStyleSheet(tema)
            janela.setWindowModality(Qt.ApplicationModal)


# inicializa a janela
        self.wMain.show()

