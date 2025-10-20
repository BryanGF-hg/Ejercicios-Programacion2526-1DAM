archivos = open("blog.txt",'r')

lineas = archivos.readlines()

for linea in lineas:
 print(linea)
