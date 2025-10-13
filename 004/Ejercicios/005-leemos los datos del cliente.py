# Declaramos una clase
class Cliente():
 def __init__(self):
  self.email = ""
  self.nombre = ""
  self.direccion = ""
#Se puede usar "" o None para definir la propiedad vacía

#Usamos la clase instanciando en un objeto
cliente1= Cliente()
cliente1.email = input("Introduce el email del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la direccion del cliente: ")

print(cliente1)
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direccion)

