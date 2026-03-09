from flask import Flask

app = Flask(__name__)

mensajes = []

@app.route("/")
def inicio():
	global mensajes
	mensajes.append("hola")
	return str(mensajes)

if __name__ == "__main__":
	app.run(debug=True)
