archivos = open("datos.csv",'r')

lineas = archivos.readlines()

for linea in lineas:
 print(linea)
