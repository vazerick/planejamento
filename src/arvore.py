from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from PyQt5.QtCore import Qt



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


class ArvoreTempoBase(Arvore):

    def atualiza(self):

        print("Arvore:")
        self.Widget.clear()
        for colecao in self.Itens.ordem:
            linha = ["Prioridade " + str(colecao['itens'][0]['prioridade'])]
            print("Espera:", self.ajeitaMes(colecao['espera']))
            linha.append(self.ajeitaMes(int(colecao['espera'])))

            WidgetItem = QTreeWidgetItem(linha)
            WidgetItem.setFlags(WidgetItem.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            WidgetItem.setCheckState(0, Qt.Unchecked)

            for item in colecao['itens']:
                child = [
                    item["nome"],
                    "R$" + str(item["preco"]),
                    str(item["prestacao"]) + "x"
                ]
                WidgetChild = QTreeWidgetItem(child)
                WidgetChild.setFlags(WidgetChild.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
                WidgetChild.setCheckState(0, Qt.Unchecked)
                WidgetItem.addChild(WidgetChild)
            self.Widget.addTopLevelItem(WidgetItem)

        self.Widget.expandAll()

        # root = self.Widget.invisibleRootItem()
        # child_count = root.childCount()
        # for i in range(child_count):
        #     print(i)
        #     item = root.child(i)
        #     item.setFlags(item.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        #     item.setCheckState(0, Qt.Unchecked)
        #     print(item)
        #     child_count2 = item.childCount()
        #     for z in range(child_count2):
        #         child = item.child(z)
        #         child.setFlags(child.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        #         child.setCheckState(0, Qt.Unchecked)

    def ler(self):

        selecionadas = []

        raiz = self.Widget.invisibleRootItem()
        cont_prior = raiz.childCount()

        for i in range(cont_prior):
            prioridade = raiz.child(i)
            cont_item = prioridade.childCount()
            print("Estado da prioridade:", prioridade.checkState(0))
            if prioridade.checkState(0):
                for z in range(cont_item):
                    item = prioridade.child(z)
                    print("Estado do item:", item.checkState(0))
                    print("Teste:", i,"-",z)

                    if item.checkState(0):
                        selecionadas.append(
                            {
                                'prioridade': i,
                                'item': z
                            }
                        )
        return selecionadas


# def getArvoreItem(item):
#     pai = item.parent().row()
#     if pai < 0:
#         pai = item.row()
#         selecionado = Prioridades.ordem[pai]
#         lerPrioridade(selecionado)
#     else:
#         filho = item.row()
#         selecionado = Prioridades.ordem[pai]['itens'][filho]
#         print(selecionado)
#         lerItemEditar(selecionado)


class ArvoreResultado():

    alerta = []

    def __init__(self, Widget, Itens, Limite, Inicio):

        self.mes = 0

        self.Widget = Widget
        self.Itens = Itens
        self.Limite = Limite
        self.Inicio = Inicio
        self.atualiza(Limite)


    def atualiza(self, Limite):

        self.Limite = Limite

        self.alerta = []

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
            mes_num = mes + self.Inicio
            while mes_num >= 12:
                mes_num -= 12
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
            if soma_mes > float(self.Limite):
                self.alerta.append(meses[mes_num])
            self.Widget.addTopLevelItem(WidgetItem)
        self.Widget.expandAll()
        print("Inicio:",self.Inicio)

    def dinheiro(self, num):
        return str("R${:.2f}".format(num))

    def percentual(self, num):
        return str(round(num*100))+"%"

