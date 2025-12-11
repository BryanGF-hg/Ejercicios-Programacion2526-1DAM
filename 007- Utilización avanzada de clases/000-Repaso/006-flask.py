# Non Playable Character
import random
import json
from flask import Flask,render_template

class Npc():
 def __init__(self,x,y):
  self.posx = x
  self.posy = y
    # Método para convertir el objeto en diccionario
 def to_dict(self):
  return {"posx": self.posx, "posy": self.posy}
#Preparo los personajes
  
personajes = []
numero_personajes = 50

for i in range(0,numero_personajes):
 x_aleatoria = random.randint(0,500)
 y_aleatoria = random.randint(0,500),
 personajes.append(Npc(x_aleatoria,y_aleatoria)) 
 
# Convertimos todos los NPC a diccionarios
personajes_json = [p.to_dict() for p in personajes]

# Lo imprimimos formateado
print(json.dumps(personajes_json, indent=2))

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
