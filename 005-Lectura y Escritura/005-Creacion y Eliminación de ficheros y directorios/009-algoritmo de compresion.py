import zipfile

origen = "archivo.txt"

destino = "ISO.zip"

archivo = zipfile.ZipFile(destino, "w", compression=zipfile.ZIP_DEFLATED)

archivo.write(origen)


