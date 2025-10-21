
'''
    Quiero:
    1.-Pedir al usuario una ruta de una carpeta con input()
    2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
    3.-Para cada archivo o carpeta, quiero comprimirla en un zip
    4.-Una vez comprimido ese ZIP, quiero eliminar los contenidos originales (opcional con booleano)
    5.-Mostrar una barra de progreso en consola con porcentaje y estimación de tiempo
'''

import os
import zipfile
import shutil
import time
import sys

def barra_progreso(iteracion, total, inicio_tiempo, longitud=40):
    """Muestra una barra de progreso con porcentaje y estimación de tiempo."""
    progreso = iteracion / total
    completado = int(longitud * progreso)
    barra = "█" * completado + "-" * (longitud - completado)
    tiempo_transcurrido = time.time() - inicio_tiempo
    if iteracion > 0:
        tiempo_estimado_total = tiempo_transcurrido / progreso
        tiempo_restante = tiempo_estimado_total - tiempo_transcurrido
    else:
        tiempo_restante = 0
    sys.stdout.write(
        f"\r[{barra}] {progreso*100:6.2f}%  "
        f"ETA: {tiempo_restante:5.1f}s"
    )
    sys.stdout.flush()


ruta_base = input("Introduce la ruta de la carpeta que quieres comprimir: ").strip()
if not os.path.exists(ruta_base):
    print("La ruta no existe.")
    exit()


respuesta = input("¿Quieres eliminar los archivos/carpetas originales después de comprimir? (s/n): ").strip().lower()
eliminar_originales = True if respuesta == "s" or respuesta == "sí" else False


# --- Recuento total de elementos para la barra de progreso ---
elementos = []
for carpeta_actual, subcarpetas, archivos in os.walk(ruta_base):
    for archivo in archivos:
        elementos.append(os.path.join(carpeta_actual, archivo))
    for subcarpeta in subcarpetas:
        elementos.append(os.path.join(carpeta_actual, subcarpeta))

total_elementos = len(elementos)
inicio_tiempo = time.time()
procesados = 0

# --- Proceso de compresión ---
for carpeta_actual, subcarpetas, archivos in os.walk(ruta_base, topdown=False):
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta_actual, archivo)
        nombre_zip = ruta_archivo + ".zip"

        with zipfile.ZipFile(nombre_zip, "w", zipfile.ZIP_DEFLATED) as zip_obj:
            zip_obj.write(ruta_archivo, os.path.basename(ruta_archivo))

        if eliminar_originales:
            os.remove(ruta_archivo)

        procesados += 1
        barra_progreso(procesados, total_elementos, inicio_tiempo)

    for subcarpeta in subcarpetas:
        ruta_subcarpeta = os.path.join(carpeta_actual, subcarpeta)
        nombre_zip = ruta_subcarpeta + ".zip"

        with zipfile.ZipFile(nombre_zip, "w", zipfile.ZIP_DEFLATED) as zip_obj:
            for carpeta_interna, subcarpetas_internas, archivos_internos in os.walk(ruta_subcarpeta):
                for archivo_interno in archivos_internos:
                    ruta_completa = os.path.join(carpeta_interna, archivo_interno)
                    arcname = os.path.relpath(ruta_completa, start=ruta_subcarpeta)
                    zip_obj.write(ruta_completa, arcname)

        if eliminar_originales:
            shutil.rmtree(ruta_subcarpeta)

        procesados += 1
        barra_progreso(procesados, total_elementos, inicio_tiempo)

print("\nProceso completado correctamente.")
