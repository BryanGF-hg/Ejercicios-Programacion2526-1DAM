import os

carpeta = input("Indica una carpeta: ")
grade = 1024*1024*1024 #1 Giga

suma = 0

for directorio,carpetas,archivos in os.walk(carpeta):
 for archivo in archivos:
  ruta = os.path.join(directorio,archivo)
  try:
   if os.path.getsize(ruta) > grande:
    print(ruta,os.path.getsize(ruta)/(1024*10),"MB")
  except:
   pass
 
