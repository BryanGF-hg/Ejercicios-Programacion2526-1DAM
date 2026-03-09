from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime

app = Flask(__name__)

mensajes = []

@app.route("/", methods=["GET", "POST"])
def inicio():
    global mensajes

    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        mensaje = request.form.get("mensaje", "").strip()

        if usuario != "" and mensaje != "":
            mensajes.append({
                "usuario": usuario,
                "mensaje": mensaje,
                "hora": datetime.now().strftime("%H:%M:%S")
            })

        return redirect("/")

    return render_template("index2.html", mensajes=mensajes)

@app.route("/mensajes")
def obtener_mensajes():
    return jsonify(mensajes)

if __name__ == "__main__":
    app.run(debug=True)
