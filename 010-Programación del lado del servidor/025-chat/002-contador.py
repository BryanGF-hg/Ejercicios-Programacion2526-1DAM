from flask import Flask

app = Flask(__name__)

contador = 1

@app.route("/")
def inicio():
	global contador
	contador += 1
	return "El contador es: "+str(contador)

if __name__ == "__main__":
	app.run(debug=True)
