# Abre una terminal e instala flask:
#pip install flask
# Flask es un microservidor web que nos permite generar HTML desde Python

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
 return "Esto es HTML desde Flask"
 
#ahora arranco el servidor
if __name__ == "__main__":
 aplicacion.run(debug=True)
