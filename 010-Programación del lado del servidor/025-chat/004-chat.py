from flask import Flask, render_template, request, redirect

app = Flask(__name__)

mensajes = []

@app.route("/", methods=["GET", "POST"])
def inicio():
    global mensajes

    if request.method == "POST":
        mensaje = request.form.get("mensaje", "").strip()
        if mensaje != "":
            mensajes.append(mensaje)
        return redirect("/")

    return render_template("index.html", mensajes=mensajes)

if __name__ == "__main__":
    app.run(debug=True)
