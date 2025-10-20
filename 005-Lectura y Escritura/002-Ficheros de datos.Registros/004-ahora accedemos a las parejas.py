import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for lineas in contenido:
 print(lineas['titulo'])
 print(lineas['fecha'])
 print(lineas['autor'])
 print(lineas['contenido'])
