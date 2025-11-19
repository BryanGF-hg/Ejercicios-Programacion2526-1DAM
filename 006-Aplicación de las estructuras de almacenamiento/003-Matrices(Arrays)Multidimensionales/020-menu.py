import pickle
agenda = []

while True:
 print("1.-Crear registro de vtuber(s)")
 print("2.-Actualizar registro de vtuber(s)")
 print("3.-Leer registro de vtuber(s)")
 print("4.-Eliminar registro de vtuber(s)")
 
 opcion = int(input("Escoge una opción: "))
 if opcion == 1:
  nombre = input("Dame tu nombre: ")
  apellidos = input("Dame tus apellidos: ")
  email = input("Dame tu email: ")
  telefono = input("Dame tu teléfono:")
  agenda.append([nombre,apellidos,email,telefono])
  archivo = open("agenda.bin","wb")
  pickle.dump(agenda,archivo)
  archivo.close()
  
 elif opcion == 2:

       
 elif opcion == 3:
  archivo = open("agenda.bin","rb")
  cadena = pickle.load(archivo)
  
  archivo.close()
  print(cadena)
 elif opcion == 4:


 else:
  break

