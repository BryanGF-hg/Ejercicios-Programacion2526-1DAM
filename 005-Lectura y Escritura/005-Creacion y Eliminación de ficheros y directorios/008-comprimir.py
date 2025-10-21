import zipfile

origen = "archivo.txt"

destino = "comprimido.zip"

archivo = zipfile.ZipFile(destino, "w")
archivo.write(origen)


