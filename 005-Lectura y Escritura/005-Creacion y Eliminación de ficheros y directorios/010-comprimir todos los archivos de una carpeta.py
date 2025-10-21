import zipfile
import os


carpeta = "archivos"

for directorio, carpetas, archivo in os.walk(carpeta):
    for nombre_archivo in archivo:
     origen = os.path.join(directorio, nombre_archivo)
     destino = os.path.join(directorio,nombre_archivo + ".zip")
     archivo = zipfile.ZipFile(destino, "w", compression=zipfile.ZIP_DEFLATED)
     archivo.write(origen, arcname=nombre_archivo)


