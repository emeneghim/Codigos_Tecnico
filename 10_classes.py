from peewee import *
import os

arq = 'base.db'
db = SqliteDatabase(arq)



if os.path.exists(arq):
    os.remove(arq)


class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
	nome  = CharField()
	idade = IntegerField()

class Console(BaseModel):
	nome = CharField()
	ano_lancamento = IntegerField()
	preco_medio = FloatField()

class Premio(BaseModel):
	tipo = CharField()
	quantidade = FloatField()

class Desenvolvedor(BaseModel):
	pessoa = ForeignKeyField(Pessoa)
	linguagem_preferida = CharField()

class Produtora(BaseModel):
	nome = CharField()
	desenvolvedores = ManyToManyField(Desenvolvedor)

class Plataforma(BaseModel):
	console = ForeignKeyField(Console)
	nome = CharField()

class Jogo(BaseModel):
	produtora = ForeignKeyField(Produtora)
	plataforma = ForeignKeyField(Plataforma)
	nome = CharField()
	genero = CharField()
	preco = FloatField()

class Jogador_profissional(BaseModel):
    pessoa = ForeignKeyField(Pessoa)
    jogo = ForeignKeyField(Jogo)
    nick = CharField()
    
class Time(BaseModel):
	jogador_profissional = ForeignKeyField(Jogador_profissional)
	jogo = ForeignKeyField(Jogo)
	nome = CharField()

class Campeonato(BaseModel):
	premio = ForeignKeyField(Premio)
	time = ForeignKeyField(Time)
	jogo = ForeignKeyField(Jogo)
	nome = CharField()


db.connect()
db.create_tables([
    Pessoa,
    Console,
    Premio,
    Desenvolvedor,
    Produtora,
    Produtora.desenvolvedores.get_through_model(),
    Plataforma,
    Jogo,
    Jogador_profissional,
    Time,
    Campeonato
])   

joao = Pessoa.create(nome="João",idade = 32)
playstation = Console.create(nome="Playstation 4", ano_lancamento = 2013, preco_medio = 2000)
premio = Premio.create(tipo="Dinheiro",quantidade = 1000)
joao_desenvolvedor = Desenvolvedor.create(pessoa=joao,linguagem_preferida="C#")
bethesda = Produtora.create(nome="Bethesda")
bethesda.desenvolvedores.add(joao_desenvolvedor)
psn = Plataforma.create(nome="PlayStation Network",console=playstation)
skyrim = Jogo.create(produtora = bethesda, plataforma = psn, nome = "Skyrim", genero = "Aventura/RPG",preco = 80)
a = Pessoa.select()
jogador = Jogador_profissional.create(pessoa = joao, jogo = skyrim, nick = "Não pensei em nada")
for b in a:
    print("nome = "+str(b.nome)+", idade = "+str(b.idade))
a = Console.select()
for b in a:
    print("nome = "+str(b.nome)+", ano de lançamento = "+str(b.ano_lancamento)+", preço médio = "+str(b.preco_medio))
a = Premio.select()
for b in a:
    print("tipo = "+str(b.tipo)+", quantidade = "+str(b.quantidade))
a = Desenvolvedor.select()
for b in a:
    print("nome = "+str(b.pessoa.nome)+", idade = "+str(b.pessoa.idade)+", linguagem preferida = "+str(b.linguagem_preferida))
a = Produtora.select()
for b in a:
    texto=("nome = "+str(b.nome))
    texto += "    | Desenvolvedores : | "
    for desenvolvedor in b.desenvolvedores:
        texto += ("nome = "+str(desenvolvedor.pessoa.nome)+", idade = "+str(desenvolvedor.pessoa.idade)+", linguagem preferida = "+str(desenvolvedor.linguagem_preferida))
    print(texto)
a = Plataforma.select()
for b in a:
    print("nome = "+str(b.nome)+"     | Console: |     Nome = "+str(b.console.nome)+", ano de lançamento = "+str(b.console.ano_lancamento)+", preço médio = "+str(b.console.preco_medio))
a = Jogo.select()
for b in a:
    print("nome = "+str(b.nome)+", genero = "+str(b.genero)+", preco = "+str(b.preco)+"     | Produtora: |    "+str(b.produtora.nome)+"      | Plataforma: |    "+str(b.plataforma.nome))
a = Jogador_profissional.select()
for b in a:
    print("nome = "+str(b.pessoa.nome)+", jogo = "+str(b.jogo.nome)+", nickname = "+str(b.nick))