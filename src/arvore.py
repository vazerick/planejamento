from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget



class Arvore:

    def __init__(self, Widget, Itens):

        self.mes = 0

        self.Widget = Widget
        self.Itens = Itens
        self.atualiza()

    def ajeitaMes(self, mes):
        mes_str = ""
        if mes == 0:
            return ""
        elif mes == 1:
            mes_str = str(mes) + " mês"
        else:
            mes_str = str(mes) + " meses"
        return "espera "+mes_str

    def adicionou(self):
        self.atualiza()
        self.Widget.expandAll()
        print()


class ArvoreItens(Arvore):

    def atualiza(self):
        print("Arvore:")
        self.Widget.clear()
        for colecao in self.Itens.ordem:
            linha = ["Prioridade " + str(colecao['itens'][0]['prioridade'])]
            print("Espera:",self.ajeitaMes(colecao['espera']))
            linha.append(self.ajeitaMes(int(colecao['espera'])))

            WidgetItem = QTreeWidgetItem(linha)

            for item in colecao['itens']:
                child = [
                    item["nome"],
                    "R$"+str(item["preco"]),
                    str(item["prestacao"])+"x"
                ]
                WidgetChild = QTreeWidgetItem(child)
                WidgetItem.addChild(WidgetChild)
            self.Widget.addTopLevelItem(WidgetItem)

        self.Widget.expandAll()

class ArvoreResultado():

    def __init__(self, Widget, Itens, Limite, Inicio):

        self.mes = 0

        self.Widget = Widget
        self.Itens = Itens
        self.Limite = Limite
        self.Inicio = Inicio
        self.atualiza()


    def atualiza(self):

        prioridades = []

        meses = [
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro',
        ]

        self.Widget.clear()

        for mes in self.Itens.Lista:
            for item in mes:
                if item[0]['prioridade'] not in prioridades:
                    prioridades.append(item[0]['prioridade'])

        for mes in range(0, len(self.Itens.Lista)):
            mes_num = mes
            while mes_num >= 12:
                mes_num -= 12
                print("Loop:", mes_num)
            print(mes_num)
            print(meses[mes_num])
            WidgetItem = QTreeWidgetItem([meses[mes_num]])

            soma_mes = 0


            for prioridade in prioridades:
                mes_prioridades = []
                for item in self.Itens.Lista[mes]:
                    if item[0]['prioridade'] == prioridade:
                        mes_prioridades.append(item[0])
                if len(mes_prioridades) > 0:

                    child = [
                        "Prioridade "+str(mes_prioridades[0]['prioridade'])
                    ]
                    WidgetChild = QTreeWidgetItem(child)

                    soma_item = 0

                    for prestacao in mes_prioridades:
                        sub_child = [
                            prestacao['nome'],
                            self.dinheiro(prestacao['preco']),
                            " " +str(prestacao['prestacao'])+"x"
                        ]
                        WidgetSubChild = QTreeWidgetItem(sub_child)
                        WidgetChild.addChild(WidgetSubChild)

                        soma_item += prestacao['preco']

                    soma_mes += soma_item

                    WidgetChild.setText(1, self.dinheiro(soma_item))
                    WidgetChild.setText(2, self.percentual(soma_item/float(self.Limite)))

                    WidgetItem.addChild(WidgetChild)
            WidgetItem.setText(1, self.dinheiro(soma_mes))
            WidgetItem.setText(2, self.percentual(soma_mes/float(self.Limite)))
            self.Widget.addTopLevelItem(WidgetItem)
        self.Widget.expandAll()
        print(self.Inicio)

    def dinheiro(self, num):
        return str("R${:.2f}".format(num))

    def percentual(self, num):
        return str(round(num*100))+"%"

