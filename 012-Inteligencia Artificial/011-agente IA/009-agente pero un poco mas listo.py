#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import requests

# ---------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------

RAIZ = "/var/www/html"   # carpeta base donde buscar

SALIDA = "/var/www/html/1DAM/@CEAC/Programacion/012-Inteligencia Artificial/011-agente IA/agente.txt"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5-coder:7b"

EXTENSIONES_TEXTO = [
    ".txt", ".py", ".js", ".php", ".html", ".css",
    ".cpp", ".c", ".java", ".json", ".md", ".xml",
    ".sql", ".sh"
]

# ---------------------------------------------------
# BUSCAR ARCHIVOS DE TEXTO
# ---------------------------------------------------

archivos_validos = []

for root, dirs, files in os.walk(RAIZ):
    for file in files:
        ruta = os.path.join(root, file)

        if any(file.lower().endswith(ext) for ext in EXTENSIONES_TEXTO):
            archivos_validos.append(ruta)

# ---------------------------------------------------
# SI NO HAY ARCHIVOS
# ---------------------------------------------------

if not archivos_validos:
    print("No se encontraron archivos válidos")
    exit()

# ---------------------------------------------------
# ELEGIR UNO ALEATORIO
# ---------------------------------------------------

archivo_elegido = random.choice(archivos_validos)

print("Archivo elegido:", archivo_elegido)

# ---------------------------------------------------
# LEER CONTENIDO
# ---------------------------------------------------

try:
    with open(archivo_elegido, "r", encoding="utf-8", errors="ignore") as f:
        contenido = f.read(4000)   # máximo 4000 chars
except:
    print("No se pudo leer")
    exit()

# ---------------------------------------------------
# ENVIAR A OLLAMA
# ---------------------------------------------------

prompt = f"""
Resume brevemente este archivo:

{contenido}
"""

payload = {
    "model": MODELO,
    "prompt": prompt,
    "stream": False
}

respuesta = requests.post(OLLAMA_URL, json=payload)

if respuesta.status_code != 200:
    print("Error Ollama")
    exit()

resumen = respuesta.json()["response"]

# ---------------------------------------------------
# GUARDAR RESULTADO
# ---------------------------------------------------

with open(SALIDA, "a", encoding="utf-8") as archivo:
    archivo.write("=====================================\n")
    archivo.write(f"Archivo: {archivo_elegido}\n")
    archivo.write(f"Resumen:\n{resumen}\n")
    archivo.write("=====================================\n\n")

print("Resumen guardado correctamente")
