

class Prioridade:

    ordem = []

    def __init__(self, Lista):
        self.Lista = Lista
        self.atualiza()

    def atualiza(self):
        self.ordem = []
        prioridades = []
        for item in self.Lista.lista:
            if item["prioridade"] not in prioridades:
                prioridades.append(item["prioridade"])
        prioridades.sort()
        for prioridade in prioridades:
            colecao = []
            for item in self.Lista.lista:
                if item["prioridade"] == prioridade:
                    colecao.append({
                        "nome": item["nome"],
                        "prioridade": item["prioridade"],
                        "preco": item["preco"],
                        "prestacao": item["prestacao"],
                        "id": item["id"],
                        "comentario": item["comentario"]
                    })
            self.ordem.append(colecao)
