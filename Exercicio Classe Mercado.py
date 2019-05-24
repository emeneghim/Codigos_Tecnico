class Carrinho():
    def __init__(self):
        self.produtos = []

class Produto():
    def __init__(self,cod_produto,valor_produto,nome):
        self.cod_produto = cod_produto
        self.valor_produto = valor_produto
        self.nome = nome

class Item():
    def __init__(self,Produto,quantidade):
        self.Produto = Produto
        self.quantidade = quantidade
    
    def retornar_valor(self):
        print(self.Produto.nome,"   Quantidade:",self.quantidade,"  Código",self.Produto.cod_produto," Custo = R$",self.Produto.valor_produto*self.quantidade)


carrinho = Carrinho()
cafe = Produto(1,5,"Café")
cenoura = Produto(2,3,"Cenoura")
kinder_ovo = Produto(3,100,"Kinder Ovo")
carrinho.produtos.append(cafe)
carrinho.produtos.append(cenoura)
carrinho.produtos.append(kinder_ovo)
for a in carrinho.produtos:
    b = float(input("Insira a quantidade do produto "+str(a.nome)+": "))
    ob_item = Item(a,b)
    ob_item.retornar_valor()