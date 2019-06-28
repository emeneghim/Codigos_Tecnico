class Mobilia():
    def __init__(self,tipo, medida, cor, preco, quantidade):
        self.tipo = tipo
        self.medida = medida
        self.cor = cor
        self.preco = preco
        self.quantidade = quantidade

class Cliente:
    def __init__(self,nome,cpf,endereco,telefone):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

class Item_pedido:
    def __init__(self,mobilia,quantidade):
        self.mobilia = mobilia
        self.quantidade = quantidade

class Pedido:
    def __init__(self):
        self.lista_mobilias = []

    def adicionar_produto(self,mobilia_item):
        mobilia = mobilia_item[0]
        qnt_item = mobilia_item[1]
        mobilia.quantidade = qnt_item 
        self.lista_mobilias.append(mobilia) 

    def mostrar_produtos(self):
        cont = 0
        for m in self.lista_mobilias:
            print (m.tipo,m.medida,m.cor,"preço: R$"+str(m.preco),"Quantidade: "+str(m.quantidade))
            cont += m.preco*m.quantidade
        print("Total a pagar: R$"+str(cont))


class Estoque:
    def __init__(self):
        self.lista_mobilias_disponiveis = []

    def adicionar_mobilia(self, mobilia, quantidade):
        for m in self.lista_mobilias_disponiveis:
            if mobilia.nome == m.nome:
                m.quantidade += quantidade
        mobilia.quantidade = quantidade
        self.lista_mobilias_disponiveis.append(mobilia)

    def remover_mobilia(self, mobilia):
        try:
            self.lista_mobilias_disponiveis.remove(mobilia)
        except:
            print("Mobilia não encontrada no estoque!")
    
    def mostrar_mobilias(self):
        for m in self.lista_mobilias_disponiveis:
            print (m.tipo,m.medida,m.cor,m.preco,m.quantidade)

cadeira = Mobilia("Cadeira","Original","Azul",50,1)
claudio = Cliente("Cláudio","111.243.989.70","Rua José das Couves","98866-0573")
pedido1 = Pedido()
estoque = Estoque()
cadeira_item = (cadeira,2)
estoque.adicionar_mobilia(cadeira,50)
estoque.mostrar_mobilias()
pedido1.adicionar_produto(cadeira_item)
estoque.mostrar_mobilias()
pedido1.mostrar_produtos()
claudio.adicionar_pedido(pedido1)
