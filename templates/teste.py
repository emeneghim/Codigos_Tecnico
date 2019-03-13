from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def teste():
    return render_template("inicio.html")

@app.route('/easter.html/')
def easter():
    return render_template('easter.html')

@app.route('/exibir_mensagem.html/')
def exibir():
    return render_template('/exibir_mensagem.html/')

@app.route('/inicio.html/')
def inicio():
    return render_template('inicio.html')

if __name__ == "__main__":
    app.run(use_reloader = True)