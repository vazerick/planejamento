import time
import xml.dom.minidom
from xml.dom import minidom


# classe geral das listas geradas pelos arquivos .xml

class Lista:

    lista = []  # lista vazia para abrigar os itens
    espera = [] #lista vazia para abrigar a espera das prioridades
    limite = 0

    def __init__(self, nome):
        self.endereco = "data/" + nome + ".xml"
        print("Abre lista ", self.endereco)

        # try:
        #     self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        # except FileNotFoundError:
        #     self.tabela = pd.DataFrame(columns=self.colunas)
        #     self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

        try:
            arquivo = xml.dom.minidom.parse(self.endereco)
        except FileNotFoundError: #todo rever a criação do primeiro xml
            arquivo = minidom.Document()  # cria um objeto xml
            # adiciona um comentário com o horário de criação
            arquivo.appendChild(doc.createComment("Criacao: %s" % time.asctime(time.localtime(time.time()))))
            lista = doc.createElement('lista')  # cria uma lista xml de doc
            arquivo.appendChild(lista)
            novo = open(self.endereco, "w", encoding='utf-8')
            novo.write(doc.toprettyxml(indent='   '))

        planejamento = arquivo.documentElement  # lê o nó <planejamento> do arquivo

        limite = planejamento.getElementsByTagName("limite")[0]  # le o nó de limite
        self.limite = limite.childNodes[0].data

        lista = planejamento.getElementsByTagName("lista")[0]  # le o nó de lista

        self.itens = lista.getElementsByTagName("item")  # gera a lista de nós de cada item
        for item in self.itens:  # para cada item da lista, cria um dicionário com os atributos definidos
            nome = item.getElementsByTagName("nome")[0]
            prioridade = item.getElementsByTagName("prioridade")[0]
            preco = item.getElementsByTagName("preco")[0]
            prestacao = item.getElementsByTagName("prestacao")[0]
            comentario = item.getElementsByTagName("comentario")[0]
            try:
                comentario_data = comentario.childNodes[0].data
            except IndexError:
                comentario_data = ""
            self.lista.append(
                {
                    'id': int(item.getAttribute("id")),
                    'nome': nome.childNodes[0].data,
                    'prioridade': int(prioridade.childNodes[0].data),
                    'preco': float(preco.childNodes[0].data),
                    'prestacao': int(prestacao.childNodes[0].data),
                    'comentario': comentario_data
                }
            )


        prioridades = planejamento.getElementsByTagName("prioridades")[0]  # le o nó de prioridades

        lista_prioridade = prioridades.getElementsByTagName("prioridade")  # gera a lista de nós de cada prioridade
        for item in lista_prioridade:  # para cada item da lista, cria um dicionário com os atributos definidos
            espera = item.getElementsByTagName("espera")[0]
            self.espera.append(
                {
                    'prioridade': int(item.getAttribute("num")),
                    'espera': int(espera.childNodes[0].data),
                }
            )


    def atualiza_prioridade(self, prioridades):
        print("Atualiza prioridade", prioridades)
        self.espera = []
        for item in prioridades:
            self.espera.append({
                'prioridade': item['prioridade'],
                'espera': item['espera']
            })
        self.salva()

    def excluir(self, id):
        print("Exlui idem ", id)
        for item in self.lista:
            if item['id']==id:
                self.lista.remove(item)
        self.salva()

    def adiciona(self, add):
        print("Adiciona ", add)
        maior = 0
        for item in self.lista:
            if item["id"] >= maior:
                maior = item["id"]+1
        add['id'] = maior
        self.lista.append(add)
        self.salva()

    def edita(self, id,
              nome,
              prioridade,
              preco,
              prestacao,
              comentario):
        print("Edita ", id)
        for item in self.lista:
            if item['id'] == id:
                item['nome'] = nome
                item['prioridade'] = int(prioridade)
                item['preco'] = float(preco)
                item['prestacao'] = int(prestacao)
                item['comentario'] = comentario
        self.salva()

    def passa_tempo(self, id):
        print("Reduz prestação de ", id)
        for item in self.lista:
            if item['id'] == id:
                if item['prestacao'] > 1:
                    item['preco'] = round(
                        item['preco'] - (item['preco'] / item['prestacao']),
                        2
                    )
                    item['prestacao'] -= 1
                else:
                    self.lista.remove(item)

    def reduz_prioridade(self, id):
        print("Reduz prioridade de ", id)
        for item in self.lista:
            if item['id'] == id:
                if item['prioridade'] > 1:
                    item['prioridade'] -= 1
                else:
                    self.lista.remove(item)


    def salva(self):
        print("Salva o arquivo ", self.endereco)
        doc = minidom.Document()  # cria um objeto xml
        # adiciona um comentário com o horário de criação
        doc.appendChild(doc.createComment("Criacao: %s" % time.asctime(time.localtime(time.time()))))

        planejamento = doc.createElement('planejamento')  # cria uma lista xml de doc

        limite = doc.createElement('limite')  # cria o nó de limite
        limite.appendChild(doc.createTextNode(self.limite))
        planejamento.appendChild(limite)

        prioridades = doc.createElement('prioridades')  # cria o nó de prioridades

        for indice in self.espera:  # adiciona cada nó na lista de doc
            prioridade = doc.createElement('prioridade')
            prioridade.setAttribute('num', str(indice['prioridade']))
            prioridades.appendChild(prioridade)

            espera = doc.createElement('espera')
            prioridade.appendChild(espera)
            espera.appendChild(doc.createTextNode(str(indice['espera'])))

        planejamento.appendChild(prioridades)

        lista = doc.createElement('lista')  # cria o nó de lista

        for indice in self.lista:  # adiciona cada nó na lista de doc
            item = doc.createElement('item')
            item.setAttribute('id', str(indice['id']))
            lista.appendChild(item)

            nome = doc.createElement('nome')
            item.appendChild(nome)
            nome.appendChild(doc.createTextNode(indice['nome']))

            prioridade = doc.createElement('prioridade')
            item.appendChild(prioridade)
            prioridade.appendChild(doc.createTextNode(str(indice['prioridade'])))

            preco = doc.createElement('preco')
            item.appendChild(preco)
            preco.appendChild(doc.createTextNode(str(indice['preco'])))

            prestacao = doc.createElement('prestacao')
            item.appendChild(prestacao)
            prestacao.appendChild(doc.createTextNode(str(indice['prestacao'])))

            comentario = doc.createElement('comentario')
            item.appendChild(comentario)
            comentario.appendChild(doc.createTextNode(str(indice['comentario'])))

        planejamento.appendChild(lista)

        doc.appendChild(planejamento)

        arquivo = open(self.endereco, "w", encoding='utf-8')
        arquivo.write(doc.toprettyxml(indent='   '))
