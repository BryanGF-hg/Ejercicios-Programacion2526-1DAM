# Non Playable Character
import random


class Npc():
 def __init__(self,x,y):
  self.posx = x
  self.posx = y
  
  
personajes = []
numero_personajes = 50

for i in range(0,numero_personajes):
 x_aleatoria = random.randint(0,500)
 y_aleatoria = random.randint(0,500),
 personajes.append(Npc(x_aleatoria,y_aleatoria)) 
 
 print(personajes)
