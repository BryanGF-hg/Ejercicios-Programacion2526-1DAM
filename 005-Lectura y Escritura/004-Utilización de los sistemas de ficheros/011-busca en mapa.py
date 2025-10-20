
archivo = open("mapa.txt","r") #READ

lineas = archivo.readlines()

for linea in lineas:
 if "py" in linea:
  print("Gotcha!: ",linea)
 else:
  pass
 
 

