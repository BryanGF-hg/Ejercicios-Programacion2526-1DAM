
'''
    Quiero:
    1.-Pedir al usuario una ruta de una carpeta con input()
    2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
    3.-Para cada archivo o carpeta, quiero comprimirla en un zip
    4.-Una vez comprimido ese ZIP, quiero eliminar los contenidos originales
'''

import os
import zipfile
import shutil

ruta_base = input("Introduce la ruta de la carpeta que quieres comprimir: ").strip()

if not os.path.exists(ruta_base):
    print("La ruta no existe.")
    exit()


for carpeta_actual, subcarpetas, archivos in os.walk(ruta_base, topdown=False):
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta_actual, archivo)
        nombre_zip = ruta_archivo + ".zip"

        zip_obj = zipfile.ZipFile(nombre_zip, "w", zipfile.ZIP_DEFLATED)
        zip_obj.write(ruta_archivo)
        zip_obj.close()

        os.remove(ruta_archivo)
        print("Archivo comprimido y eliminado:", ruta_archivo)


    for subcarpeta in subcarpetas:
        ruta_subcarpeta = os.path.join(carpeta_actual, subcarpeta)
        nombre_zip = ruta_subcarpeta + ".zip"

        zip_obj = zipfile.ZipFile(nombre_zip, "w", zipfile.ZIP_DEFLATED)

        for carpeta_interna, subcarpetas_internas, archivos_internos in os.walk(ruta_subcarpeta):
            for archivo_interno in archivos_internos:
                ruta_completa = os.path.join(carpeta_interna, archivo_interno)
                zip_obj.write(ruta_completa)

        zip_obj.close()

        #Elimina el resto de subcarpetas rapidamente
        shutil.rmtree(ruta_subcarpeta)
        print("Carpeta comprimida y eliminada:", ruta_subcarpeta)

print("Proceso completado correctamente.")

