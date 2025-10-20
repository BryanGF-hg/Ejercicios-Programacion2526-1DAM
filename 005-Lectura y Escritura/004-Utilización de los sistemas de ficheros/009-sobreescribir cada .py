import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024 #1 Giga

mapa = open("mapa.txt","w") # Sobre escribe el archivo mapa.txt

for directorio,carpetas,archivos in os.walk(carpeta):
 for archivo in archivos:
  ruta = os.path.join(directorio,archivo)
  mapa.write(ruta+"\n")
  
  
mapa.close()
 
