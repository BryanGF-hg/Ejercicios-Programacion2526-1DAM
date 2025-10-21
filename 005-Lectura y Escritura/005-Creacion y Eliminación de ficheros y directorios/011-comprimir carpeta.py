import zipfile
import os

origen = "archivos"
destino = "archivos.zip"

archivozip = zipfile.ZipFile(destino,"w", zipfile.ZIP_DEFLATED)
for directorio, carpetas, archivo in os.walk(origen):
 for archivo in archivo:
  rutaarchivo = os.path.join(directorio,archivo)
  rutarelativa = os.path.relpath(rutaarchivo,origen)
  archivozip.write(rutaarchivo, rutarelativa)

archivozip.close()
  

