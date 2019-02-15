import sys
import sass

# import do PyQt5

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget


from src.gui import gui
from src.lista import Lista
from src.prioridade import Prioridade
from src.arvore import Arvore, ArvoreItens, ArvoreResultado


def atualiza():
    Prioridades.atualiza()
    ArvoreItens.atualiza()


def botao_adicionar():
    Gui.ui.stackedWidget.setCurrentIndex(1)


def botao_adicionar_adicionar():
    nome = Gui.ui.lineAddNome.text()
    preco = Gui.ui.spinAddPreco.value()
    prestacao = Gui.ui.spinAddPrestacoes.value()
    prioridade = Gui.ui.spinAddPrioridade.value()
    comentario = Gui.ui.textAddComentarios.toPlainText()
    print(nome, preco, prestacao, prioridade, comentario)
    if nome!="" and prestacao > 0 and preco > 0 and prioridade > 0:
        Lista.adiciona({
            "nome": nome,
            "preco": preco,
            "prestacao": prestacao,
            "prioridade": prioridade,
            "comentario": comentario,
        })
        atualiza()
        mensagem(
            titulo="Item Adicionado",
            mensagem="Item "+nome+" adicionado com sucesso.",
            ui=Gui.uiOk,
            janela=Gui.wOk
        )


def botao_adicionar_cancelar():
    Gui.ui.stackedWidget.setCurrentIndex(0)
    Gui.ui.lineAddNome.clear()
    Gui.ui.textAddComentarios.clear()
    Gui.ui.spinAddPreco.clear()
    Gui.ui.spinAddPrestacoes.clear()
    Gui.ui.spinAddPrioridade.clear()


def botao_excluir():
    selecionado = Gui.ui.treeItens.currentIndex()
    pai = selecionado.parent().row()
    filho = selecionado.row()
    id = Prioridades.ordem[pai][filho]["id"]
    Lista.excluir(Lista.lista[id])
    atualiza()
    Gui.wExcluir.hide()


def botao_desfazer():
    Gui.ui.stackedWidget.setCurrentIndex(0)



def mensagem(titulo, mensagem, ui, janela):
    ui.labelTitulo.setText(titulo)
    ui.labelMensagem.setText(mensagem)
    janela.show()


def getArvoreItem(item):
    pai = item.parent().row()
    if pai < 0:
        pai = item.row()
        selecionado = Prioridades.ordem[pai]
        lerPrioridade(selecionado)
    else:
        filho = item.row()
        selecionado = Prioridades.ordem[pai][filho]
        print(selecionado)
        lerItemEditar(selecionado)


def lerPrioridade(prioridade):
    Gui.ui.listItens.clear()
    Gui.ui.stackedWidget.setCurrentIndex(3)
    Gui.ui.labelPrioridade.setText(str(prioridade[0]["prioridade"]))
    for item in prioridade:
        linha = [item["nome"]]
        WidgetItem = QTreeWidgetItem(linha)
        child = [
            "R$"+str(item["preco"]),
            str(item["prestacao"]) + "x"
        ]
        WidgetChild = QTreeWidgetItem(child)
        WidgetItem.addChild(WidgetChild)
        Gui.ui.listItens.addTopLevelItem(WidgetItem)
        Gui.ui.listItens.expandAll()


def lerItemEditar(item):
    Gui.ui.stackedWidget.setCurrentIndex(2)
    Gui.ui.lineNome.setText(item["nome"])
    Gui.ui.textComentarios.setText(item["comentario"])
    Gui.ui.spinPreco.setValue(item["preco"])
    Gui.ui.spinPrestacoes.setValue(item["prestacao"])
    Gui.ui.spinPrioridade.setValue(item["prioridade"])

def muda_limite():
    Lista.limite = str(Gui.ui.spinLimite.value())
    Lista.salva()
    atualiza()
    print(Lista.limite)

def foo(bar):
    print(bar)


Gui = gui()
Gui.ui.labelInstrucoes.setText(
    "Instruções:\n" +
    "\tAdicione itens"
)
Gui.ui.stackedWidget.setCurrentIndex(0)

Lista = Lista("lista")
Gui.ui.spinLimite.setValue(float(Lista.limite))


Prioridades = Prioridade(Lista)
ArvoreItens = ArvoreItens(Gui.ui.treeItens, Prioridades)

Gui.ui.buttonAdicionar.clicked.connect(botao_adicionar)
Gui.ui.buttonAddAdicionar.clicked.connect(botao_adicionar_adicionar)
Gui.ui.buttonCancelar.clicked.connect(botao_adicionar_cancelar)
Gui.ui.buttonDesfazer.clicked.connect(botao_desfazer)
Gui.ui.buttonExcluir.clicked.connect(lambda: mensagem(
    titulo="Excluir item?",
    mensagem="Tem certeza que deseja excluir " + Gui.ui.lineNome.text() + "?\n Essa ação não poderá ser desfeita",
    ui=Gui.uiExcluir,
    janela=Gui.wExcluir
))


Gui.uiOk.pushButton.clicked.connect(Gui.wOk.hide)
Gui.uiExcluir.buttonBox.rejected.connect(Gui.wExcluir.hide)
Gui.uiExcluir.buttonBox.accepted.connect(botao_excluir)

Gui.ui.treeItens.clicked.connect(getArvoreItem)

Gui.ui.spinLimite.editingFinished.connect(muda_limite)

Lista.salva()

sys.exit(Gui.app.exec_())

