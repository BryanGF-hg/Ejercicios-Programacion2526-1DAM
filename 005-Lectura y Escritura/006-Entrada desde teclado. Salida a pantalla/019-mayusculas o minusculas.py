class Cliente():
 def __init__(self,nombre,apellidos,email):
  self.nombre = nombre
  self.apellidos = apellidos
  self.email = email
 
print("#####Gestión de clientes v0.1#####")
print("#####    Bryan Glot Fong    ######")

#Esto es un array o lista que empieza con un elemento 0 si se añade algo de cualquier metodo, entonces empezaría con el elemento 1
clientes = []

while True:
 print("Escoge una opción: ")
 print("1.-Insertar un cliente")
 print("2.-Listar clientes")
 print("3.-Actualizar un cliente")
 print("4.-Eliminar un cliente\n")

 opcion = int(input("Escoge una opción: "))
 
 if opcion == 1:
  nombre = input("Introduce el nombre: ")
  apellidos = input("Introduce los apellidos: ")
  email = input("Introduce el email: ")
  clientes.append(Cliente(nombre,apellidos,email))
  
 elif opcion == 2:
  identificador = 0
  for cliente in clientes:
   print("Este es el cliente con ID:",identificador)
   print(cliente.nombre,cliente.apellidos,cliente.email)
   identificador += 1
   
 elif opcion == 3:
  identificador = int(input("Introduce el id para identificar: "))
  nombre = input("Introduce el nombre: ")
  apellidos = input("Introduce los apellidos: ")
  email = input("Introduce el email: ")
  clientes[identificador].nombre = nombre
  clientes[identificador].apellidos = apellidos
  clientes[identificador].email = email
  
 elif opcion == 4:
  identificador = int(input("Introduce el id para identificar: "))
  confirmacion = input("Estás seguro? (S/N)")
  
   if confirmacion == "S" or confirmacion == "s":
   clientes.splice(identificador,1)
   elif confirmacion == "N" or confirmacion =="n":
    print("cancelado")
   else:
    print("Opción no valida")
