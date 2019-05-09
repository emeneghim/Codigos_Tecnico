from flask import Flask, render_template, request, session, redirect
app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "Meneghim"

lista = [("Joao","Rua 9", "3322-5152"),
         ("Maria","Rua 11", "99982-7080"),
         ("Eugenia", "Rua 13", "3028-5612")]
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
    print ("Teste 2")
    nova = (nome, ender, tel)
    lista.append(nova)
    return render_template('exibir_mensagem.html', lista = lista)

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