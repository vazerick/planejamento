import sys
import sass

# import do PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt

# import das janelas

from ui.main import Ui_MainWindow as Main
from ui.excluir import Ui_Form as Excluir
from ui.sucesso import Ui_Form as Ok
from ui.tempo import Ui_Form as Tempo
from ui.grafico import Ui_Form as Grafico

class gui:

    def __init__(self):
# declarações da interface gráfica
        print("Gerando a interface gráfica")

        self.app = QApplication(sys.argv)

# janela principal
        self.wMain = QMainWindow()
        self.ui = Main()
        self.ui.setupUi(self.wMain)
        
        self.wGrafico = QDialog()
        self.uiGrafico = Grafico()
        self.uiGrafico.setupUi(self.wGrafico)

        self.wTempo = QDialog()
        self.uiTempo = Tempo()
        self.uiTempo.setupUi(self.wTempo)

        self.wTempoPrioridade = QDialog()
        self.uiTempoPrioridade = Tempo()
        self.uiTempoPrioridade.setupUi(self.wTempoPrioridade)

        self.ui.treeItens.setColumnWidth(0, 175)
        self.ui.treeResultado.setColumnWidth(0, 200)
        self.uiTempo.listItens.setColumnWidth(0, 230)
        self.uiTempoPrioridade.listItens.setColumnWidth(0, 230)

        self.wExcluir = QDialog()
        self.uiExcluir = Excluir()
        self.uiExcluir.setupUi(self.wExcluir)

        self.wOk = QDialog()
        self.uiOk = Ok()
        self.uiOk.setupUi(self.wOk)


# seta a mesma folha de estilos e bloqueio para todas as janelas


        tema = sass.compile(filename="ui/style.scss")
        print("Gera o tema", tema)

        self.wMain.setStyleSheet(tema)
        self.wMain.show()


        for janela in [
            self.wMain,
            self.wExcluir,
            self.wOk,
            self.wTempo,
            self.wTempoPrioridade,
            self.wGrafico
        ]:
            janela.setStyleSheet(tema)
            janela.setWindowModality(Qt.ApplicationModal)


# inicializa a janela
        self.wMain.show()

