class Gato():
 def __init__(self,edad,nombre):    # El constructor se ejecuta si o si
  self.edad = 0
  self.nombre = nombre
  
 def maulla(self): # El resto de métodos sólo se ejecutan si los llamas
  return "El gato está maullando"
  
  
gato1 = Gato(5,"micifu")



