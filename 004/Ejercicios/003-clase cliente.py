# Declaramos una clase
class Cliente():
 def __init__(self):
  self.email = ""
  self.nombre = ""
  self.direccion = ""
#Se puede usar "" o None para definir la propiedad vacía

#Usamos la clase instanciando en un objeto
cliente1= Cliente()
cliente1.email = "jose@empresa.com"
cliente1.nombre = "Jose"
cliente1.direccion = "La calle de Jose"


