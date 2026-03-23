from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/inventario")
def inventario():
    return render_template("inventario.html")

@app.route("/envios")
def envios():
    return render_template("envios.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))