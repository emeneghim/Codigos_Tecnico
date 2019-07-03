import os
from peewee import *

db = SqliteDatabase("mene.db")
db.connect()

class BaseModel(Model):
    class Meta:
        database = db
    
class Registro(BaseModel):
    data = DateTimeField()
    ocorrencia = CharField()
    intensidade = CharField()
    observacoes = CharField()

db.create_tables([Registro])
a = Registro(data = "03/07/2019", ocorrencia = "Ataque Cardíaco", intensidade = "Forte", observacoes ="Quase morri")

a.save()