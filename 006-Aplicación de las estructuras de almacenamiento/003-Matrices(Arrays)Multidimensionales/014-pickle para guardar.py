import pickle
agenda = []

while True:
 nombre = input("Dame tu nombre: ")
 apellidos = input("Dame tus apellidos: ")
 email = input("Dame tu email: ")
 telefono = input("Dame tu teléfono: ")
 #Añado a la agenda
 agenda.append([nombre,apellidos,email,telefono])
 print(agenda)
 archivo = open("agenda.bin","wb")
 pickle.dump(agenda,archivo) #Primero lo que cuelgas (cosa), # Segundo donde lo cuelgas (locación)
 archivo.close()
 
