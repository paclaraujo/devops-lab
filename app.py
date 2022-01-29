from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Aula 1- Devops Lab"

if __name__ == '__main__':
    app.run()