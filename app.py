from flask import Flask, render_template, request
from buscador import buscar
from extrator import extrair_texto
from personalidade import dar_personalidade

app = Flask(__name__)

def agente(pergunta):
    resultados = buscar(pergunta)
    if not resultados:
        return "Não encontrei nada sobre isso."
    texto = extrair_texto(resultados[0]["link"])
    return dar_personalidade(pergunta, texto)

@app.route("/")
def home():
    return render_template("webserver.html", resposta=None)

@app.route("/perguntar", methods=["POST"])
def perguntar():
    pergunta = request.form["pergunta"]
    resposta = agente(pergunta)
    return render_template("webserver.html", resposta=resposta)

if __name__ == "__main__":
    app.run(debug=True)