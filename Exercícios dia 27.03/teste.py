
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')

lista = [("Joao","Rua 9", "3322-5152"),
         ("Maria","Rua 11", "99982-7080"),
         ("Eugenia", "Rua 13", "3028-5612")]
@app.route("/", methods=['POST','GET'])
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

@app.route('/incluir_pessoa')
def incluir_pessoa():
    nome = request.args.get("nome")
    ender = request.args.get("endereco")
    tel = request.args.get("telefone")
    print ("Teste 2")
    nova = (nome, ender, tel)
    lista.append(nova)
    return render_template('exibir_mensagem.html', lista = lista)

if __name__ == "__main__":
    app.run(use_reloader = True)