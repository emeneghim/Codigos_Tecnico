from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route('/easter/')
def easter():
    return render_template('easter.html')

@app.route('/exibir_mensagem/')
def exibir():
    return render_template('exibir_mensagem.html')

if __name__ == "__main__":
    app.run(use_reloader = True)