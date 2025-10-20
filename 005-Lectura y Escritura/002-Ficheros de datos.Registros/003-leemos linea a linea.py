import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for lineas in contenido:
 print(lineas)
