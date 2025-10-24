class Cliente():
 def __init__(self,nombre,apellidos,email):
  self.nombre = nombre
  self.apellidos = apellidos
  self.email = email
 
print("#####Gestión de clientes v0.1#####")
print("#####    Bryan Glot Fong    ######")

clientes = []

while True:
 print("Escoge una opción: ")
 print("1.-Insertar un cliente")
 print("2.-Listar clientes")
 print("3.-Actualizar un cliente")
 print("4.-Eliminar un cliente\n")

 opcion = int(input("Escoge una opción: "))
 
