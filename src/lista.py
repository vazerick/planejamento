import time
import xml.dom.minidom
from xml.dom import minidom


# classe geral das listas geradas pelos arquivos .xml

class Lista:

    lista = []  # lista vazia para abrigar os itens
    limite = 0

    def __init__(self, nome):
        self.endereco = "data/" + nome + ".xml"

        # try:
        #     self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        # except FileNotFoundError:
        #     self.tabela = pd.DataFrame(columns=self.colunas)
        #     self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

        try:
            arquivo = xml.dom.minidom.parse(self.endereco)
        except FileNotFoundError:
            arquivo = minidom.Document()  # cria um objeto xml
            # adiciona um comentário com o horário de criação
            arquivo.appendChild(doc.createComment("Criacao: %s" % time.asctime(time.localtime(time.time()))))
            lista = doc.createElement('lista')  # cria uma lista xml de doc
            arquivo.appendChild(lista)
            novo = open(self.endereco, "w", encoding='utf-8')
            novo.write(doc.toprettyxml(indent='   '))
        lista = arquivo.documentElement  # lê o nó <lista> do arquivo

        limite = lista.getElementsByTagName("limite")[0]  # le o nó de limite
        self.limite = limite.childNodes[0].data

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

    def excluir(self, item):
        self.lista.remove(item)
        self.salva()

    def adiciona(self, add):
        maior = 0
        for item in self.lista:
            print(item)
            if item["id"] >= maior:
                maior = item["id"]+1
                print("Id:",item["id"])
                print("Maior:", maior)
        add['id'] = maior
        print("Add:",add)
        self.lista.append(add)
        self.salva()


    def salva(self):
        doc = minidom.Document()  # cria um objeto xml
        # adiciona um comentário com o horário de criação
        doc.appendChild(doc.createComment("Criacao: %s" % time.asctime(time.localtime(time.time()))))

        lista = doc.createElement('lista')  # cria uma lista xml de doc

        limite = doc.createElement('limite')  # cria o nó de limite
        limite.appendChild(doc.createTextNode(self.limite))
        lista.appendChild(limite)

        for indice in self.lista:  # adiciona cada nó na lista de doc
            print("Salva:", indice)
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

        doc.appendChild(lista)

        arquivo = open(self.endereco, "w", encoding='utf-8')
        arquivo.write(doc.toprettyxml(indent='   '))
