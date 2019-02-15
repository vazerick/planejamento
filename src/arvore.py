from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
import pandas



class Arvore:

    def __init__(self, Widget, Itens):

        self.mes = 0

        self.Widget = Widget
        self.Itens = Itens
        self.atualiza()

    def ajeitaMes(self):
        if self.mes == 1:
            return str(self.mes) + " mês"
        else:
            return str(self.mes) + " meses"

    def adicionou(self):
        self.atualiza()
        self.Widget.expandAll()
        print()

class ArvoreItens(Arvore):

    def atualiza(self):
        print("Arvore:")
        self.Widget.clear()
        for colecao in self.Itens.ordem:
            linha = ["Prioridade " + str(colecao[0]['prioridade'])]
            linha.append(self.ajeitaMes())

            WidgetItem = QTreeWidgetItem(linha)

            for item in colecao:
                child = [
                    item["nome"],
                    "R$"+str(item["preco"]),
                    str(item["prestacao"])+"x"
                ]
                WidgetChild = QTreeWidgetItem(child)
                WidgetItem.addChild(WidgetChild)
            self.Widget.addTopLevelItem(WidgetItem)

class ArvoreResultado(Arvore):

    def atualiza(self):
        print(a)