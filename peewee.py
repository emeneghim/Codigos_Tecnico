import os
from peewee import *
db1 = 'many.db'
db = SqliteDatabase(db1)

class BaseModel(Model):
    class Meta:
        database = db

class Disciplina(BaseModel):
    nome = CharField()

class Aluno(BaseModel):
    nome = CharField()
    disciplinas = ManyToManyField(Disciplina)

if os.path.exists(db1):
    os.remove(db1)

db.connect()
db.create_tables([Aluno, 
            Disciplina,
            Aluno.disciplinas.get_through_model()])

joao = Aluno.create(nome="Joao")
ingles = Disciplina.create(nome = "Ingles I")
joao.disciplinas.add(ingles)
maria = Aluno.create(nome="Maria")
maria.disciplinas.add(ingles)
todos_alunos = Aluno.select()
for aluno in todos_alunos:
    a = aluno.nome
    for disciplina in aluno.disciplinas:
        print(a,disciplina.nome)