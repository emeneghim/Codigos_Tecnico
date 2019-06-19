from flask import Flask, render_template, request, session, redirect
from peewee import *
import os
app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "Meneghim"
db = SqliteDatabase('many.db')
lista = []

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()

if os.path.exists('many.db'):
    os.remove('many.db')
db.connect()
db.create_tables([Pessoa])

todas_pessoas = Pessoa.select()
for pessoa in todas_pessoas:
    print (pessoa.nome)


@app.route("/")
def inicio():
    return render_template("inicio.html", lista = lista)

@app.route('/easter/')
def easter():
    return render_template('easter.html', lista = lista)

@app.route('/exibir_mensagem/')
def exibir():
    return render_template('exibir_mensagem.html', lista = lista)

@app.route('/listar_pessoas/')
def listar_pessoas():
    return render_template('listar_pessoas.html', lista = lista)

@app.route('/incluir_pessoa', methods = ["POST"])
def incluir_pessoa():
    nome = request.form["nome"]
    ender = request.form["endereco"]
    tel = request.form["telefone"]
    #nova = (nome, ender, tel)
    #lista.append(nova)
    Pessoa.create(nome =request.form["nome"],endereco=request.form["endereco"],telefone=request.form["telefone"])
    lista = Pessoa.select()
    return render_template('exibir_mensagem.html', lista = Pessoa.select())

@app.route("/excluir_pessoa")
def excluir():
    achou = None
    nome = request.args.get("nome")
    for p in lista:
        if p[0] == nome:
            achou = p
            break
    if achou != None and session["usuario"]: 
        lista.remove(achou)
    return render_template('exibir_mensagem.html', lista = lista)    

@app.route("/form_alterar_pessoa")
def form_alterar_pessoa():
    procurado = request.args.get("nome")
    for pe in lista:
        if pe[0] == procurado:
            pessoa = pe
            print(pessoa)
    return "não achei: " +str(procurado)

@app.route("/login", methods = ["POST"])
def login():
    login = request.form["login"]
    senha = request.form["senha"]
    if login == "dudu" and senha == "123":
        session["usuario"] = login
        return redirect("/")
    else:
        return ("login/senha inválidos!")

@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect("/")

if __name__ == "__main__":
    app.run(use_reloader = True, debug = True)  