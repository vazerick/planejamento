import sys
import sass
import time

# import do PyQt5

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget


from src.gui import gui
from src.lista import Lista
from src.prioridade import Prioridade
from src.arvore import Arvore, ArvoreItens, ArvoreTempoBase, ArvoreResultado
from src.resultado import Resultado


def atualiza():
    Prioridades.atualiza()
    ArvorePrioridades.atualiza()
    Resultado.atualiza(Lista.limite, Prioridades.ordem)
    ArvoreResultado.atualiza(Lista.limite)
    ArvoreTempo.atualiza()
    ArvoreTempoPrioridade.atualiza()
    confere_limite()


def botao_ok():
    Gui.wOk.hide()
    Gui.ui.lineAddNome.setFocus()


def botao_tempo_ok():
    selecionados = ArvoreTempoBase.ler()
    print(selecionados)
    for item in selecionados:
        id = Prioridades.ordem[item['prioridade']]['itens'][item['item']]['id']
        print(id)
        Lista.passa_tempo(id)
    Lista.salva()
    atualiza()


def botao_tempoprioridade_ok():
    selecionados = ArvoreTempoPrioridade.ler()
    print(selecionados)
    for item in selecionados:
        id = Prioridades.ordem[item['prioridade']]['itens'][item['item']]['id']
        print(id)
        Lista.reduz_prioridade(id)
    Lista.salva()
    atualiza()


def botao_adicionar():
    Gui.ui.stackedWidget.setCurrentIndex(1)
    Gui.ui.spinAddPrestacoes.setValue(1)
    Gui.ui.spinAddPrioridade.setValue(1)


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
        limpar = [
            Gui.ui.lineAddNome,
            Gui.ui.spinAddPreco,
            Gui.ui.spinAddPrestacoes,
            Gui.ui.spinAddPrioridade,
            Gui.ui.textAddComentarios
        ]
        for item in limpar:
            item.clear()


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
    id = Prioridades.ordem[pai]['itens'][filho]["id"]
    Lista.excluir(id)
    atualiza()
    Gui.wExcluir.hide()


def botao_desfazer():
    Gui.ui.stackedWidget.setCurrentIndex(0)



def mensagem(titulo, mensagem, ui, janela):
    ui.labelTitulo.setText(titulo)
    ui.labelMensagem.setText(mensagem)
    janela.show()

def botao_tempo():
    Gui.uiTempo.labelTitulo.setText("Passar Tempo - Prestação")
    Gui.uiTempo.labelMensagem.setText(
        "Selecione os itens para remover uma prestação deles\n"
        "Itens com uma prestação selecionados serão deletados"
    )
    Gui.wTempo.show()


def botao_tempoprioridade():
    Gui.uiTempoPrioridade.labelTitulo.setText("Passar Tempo - Prioridade")
    Gui.uiTempoPrioridade.labelMensagem.setText(
        "Selecione os itens para diminuir a Prioridade em um nivel\n"
        "Itens de Prioridade 1 selecionados serão deletados"
    )
    Gui.wTempoPrioridade.show()


def botao_salvar():
    print("salvar")
    item = Gui.ui.treeItens.currentIndex()
    pai = item.parent().row()
    filho = item.row()
    selecionado = Prioridades.ordem[pai]['itens'][filho]
    print(selecionado['id'])

    dados = {
        'nome': "Nome",
        'prioridade': 0,
        'preco': 0,
        'prestacao': 0,
        'comentario': "Comentario"
    }

    print(dados)

    Lista.edita(
        id=selecionado['id'],
        nome=Gui.ui.lineNome.text(),
        prioridade=Gui.ui.spinPrioridade.value(),
        preco=Gui.ui.spinPreco.value(),
        prestacao=Gui.ui.spinPrestacoes.value(),
        comentario=Gui.ui.textComentarios.toPlainText()
    )
    atualiza()

def botao_prioridade_salvar():
    print("salvar")
    item = Gui.ui.treeItens.currentIndex().row()
    Prioridades.ordem[item]['espera'] = Gui.ui.spinEspera.value()
    Lista.atualiza_prioridade(Prioridades.ordem)
    atualiza()


def getArvoreItem(item):
    pai = item.parent().row()
    if pai < 0:
        pai = item.row()
        selecionado = Prioridades.ordem[pai]
        lerPrioridade(selecionado)
    else:
        filho = item.row()
        selecionado = Prioridades.ordem[pai]['itens'][filho]
        print(selecionado)
        lerItemEditar(selecionado)


def lerPrioridade(prioridade):
    Gui.ui.listItens.clear()
    Gui.ui.stackedWidget.setCurrentIndex(3)
    Gui.ui.labelPrioridade.setText(str(prioridade['itens'][0]["prioridade"]))
    Gui.ui.spinEspera.setValue(int(prioridade['espera']))
    for item in prioridade['itens']:
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


def lerItemResultado(item):
    avo = item.parent().row()
    if avo < 0:
        selecionado = Resultado.Lista[item.row()]
        print(selecionado)
    else:
        selecionado = Gui.ui.treeResultado.currentItem().text(0)
        find = Gui.ui.treeItens.findItems(selecionado, Qt.MatchContains | Qt.MatchRecursive, 0)
        for x in find:
            print(x)
            Gui.ui.treeItens.setCurrentItem(x)

        # filho = item.row()
        # selecionado = Prioridades.ordem[pai]['itens'][filho]
        # print("Filho",selecionado)

def muda_mes():
    ArvoreResultado.Inicio=Gui.ui.comboMes.currentIndex()
    atualiza()

def muda_limite():
    Lista.limite = str(Gui.ui.spinLimite.value())
    Lista.salva()
    atualiza()
    print(Lista.limite)

def instrucoes_padrao():
    Gui.ui.labelInstrucoes.setText(
        "Instruções:\n" +
        "\tAdicione itens"
    )

def instrucoes_alerta(meses):
    texto = ("Alerta:\n" +
        "\tGastos excessivos nos meses")
    for mes in meses:
        texto = texto + "\n\t\t" + mes
    Gui.ui.labelInstrucoes.setText(texto)

def confere_limite():
    alerta = ArvoreResultado.alerta
    print(alerta)
    if len(alerta) > 0:
        instrucoes_alerta(alerta)
        Gui.ui.stackedWidget.setCurrentIndex(0)
    else:
        instrucoes_padrao()

Gui = gui()
instrucoes_padrao()
Gui.ui.stackedWidget.setCurrentIndex(0)

Lista = Lista("lista")
Gui.ui.spinLimite.setValue(float(Lista.limite))


Prioridades = Prioridade(Lista)
ArvorePrioridades = ArvoreItens(Gui.ui.treeItens, Prioridades)

Gui.ui.buttonAdicionar.clicked.connect(botao_adicionar)
Gui.ui.buttonAddAdicionar.clicked.connect(botao_adicionar_adicionar)
Gui.ui.buttonCancelar.clicked.connect(botao_adicionar_cancelar)
Gui.ui.buttonDesfazer.clicked.connect(botao_desfazer)
Gui.ui.buttonSalvar.clicked.connect(botao_salvar)
Gui.ui.buttonPrioridadeSalvar.clicked.connect(botao_prioridade_salvar)

Gui.ui.buttonTempo.clicked.connect(botao_tempo)
Gui.ui.buttonTempoPrioridade.clicked.connect(botao_tempoprioridade)

Gui.ui.buttonExcluir.clicked.connect(lambda: mensagem(
    titulo="Excluir item?",
    mensagem="Tem certeza que deseja excluir " + Gui.ui.lineNome.text() + "?\n Essa ação não poderá ser desfeita",
    ui=Gui.uiExcluir,
    janela=Gui.wExcluir
))


Gui.uiOk.pushButton.clicked.connect(botao_ok)
Gui.uiExcluir.buttonBox.rejected.connect(Gui.wExcluir.hide)
Gui.uiExcluir.buttonBox.accepted.connect(botao_excluir)

Gui.ui.treeItens.clicked.connect(getArvoreItem)

Gui.ui.treeResultado.clicked.connect(lerItemResultado)


Gui.ui.spinLimite.editingFinished.connect(muda_limite)

Gui.ui.comboMes.setCurrentIndex(
    time.localtime(time.time()).tm_mon-1
)

Gui.ui.comboMes.currentIndexChanged.connect(muda_mes)

Lista.salva()

Resultado = Resultado(Lista.limite, Prioridades.ordem)
ArvoreResultado = ArvoreResultado(Gui.ui.treeResultado, Resultado, Lista.limite, Gui.ui.comboMes.currentIndex())


ArvoreTempo = ArvoreTempoBase(Gui.uiTempo.listItens, Prioridades)
Gui.uiTempo.pushButton.clicked.connect(botao_tempo_ok)

ArvoreTempoPrioridade = ArvoreTempoBase(Gui.uiTempoPrioridade.listItens, Prioridades)
Gui.uiTempoPrioridade.pushButton.clicked.connect(botao_tempoprioridade_ok)

confere_limite()

sys.exit(Gui.app.exec_())

