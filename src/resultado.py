
class Resultado:

    Limite = 0
    Lista = []


    def __init__(self, limite, prioridades):
        self.Limite = limite
        self.Prioridades = prioridades
        self.atualiza(limite, prioridades)


    def atualiza(self, limite, prioridades):

        self.Limite = limite
        self.Prioridades = prioridades

        Meses = []
        mes_cont = 0

        espera_acumulada = 0

        for prioridade in self.Prioridades:
            mes_inicial = prioridade['espera'] + espera_acumulada
            espera_acumulada += prioridade['espera']
            for item in prioridade['itens']:
                total = mes_inicial + item['prestacao'] + item['prioridade']
                mes_cont = max(mes_cont, total)

        while len(Meses) < mes_cont:
            Meses.append([])

        espera_acumulada = 0

        for prioridade in self.Prioridades:
            mes_inicial = prioridade['espera'] + prioridade['prioridade'] + espera_acumulada - 1
            espera_acumulada += prioridade['espera']
            for item in prioridade['itens']:
                preco = item['preco'] / item['prestacao']
                for cont in range(0, item['prestacao']):
                    print("Meses:\n"+"Tamanho:",len(Meses),"Mês:",mes_inicial + cont)
                    Meses[mes_inicial + cont].append([{
                        'nome': item['nome'],
                        'prioridade': item['prioridade'],
                        'preco': preco,
                        'prestacao': item['prestacao'] - cont
                    }])

        self.Lista = Meses
        for item in self.Lista:
            print(item)




        #
        #
        #             try:
        #                 if len(Mes[prestacao]) == 0:
        #                     print("AAAA: ",Mes,"\n\t",len(Mes))
        #                     Mes[prestacao]['item'].append({
        #                         'nome': item['nome'],
        #                         'preco': item['preco'],
        #                         'prestacao': item['prestacao'] - prestacao
        #                     })
        #             except KeyError:
        #                 Mes[prestacao] = {
        #                     'prioridade': prioridade['prioridade'],
        #                     'item': [{
        #                         'nome': item['nome'],
        #                         'preco': item['preco'],
        #                         'prestacao': item['prestacao'] - prestacao
        #                     }]
        #                 }
        # for x in Mes:
        #     print("Mes:",x)



#####################################################################################################################
# Como fazer?
#####################################################################################################################
# Fazer uma lista com objetos para todos os meses.
# Começa na primeira Prioridade, e adiciona ao mês em questão os itens, e reduz em 1 o número de prestações
# Depois, vai para o mês seguinte. E le desde a primeira Prioridade, e também da próxima Prioridade.
# Assim por diante.
# Para quando tiver um mês vazio, e não tiver nenhuma prioridade na espera.
#####################################################################################################################
# Fazer uma lista com objetiso para todos os meses.
# Começa na primeira Prioridade, e no primeiro item. Adiciona todas as prestações desse item nos meses necessários.
# Depois, vai para o item seguinte. Até terminar. Aí vai para a próxima Prioridade. Até terminar tudo.
# Essa alternativa vai usar menos loops, provavelmente.
#####################################################################################################################
