#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import os
import subprocess
import sys
import time
import requests

# ---------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------

MODELO = "qwen2.5-coder:7b"
URL = "http://localhost:11434/api/generate"

PROMPT = """
Genera únicamente código Python válido.
El programa debe sumar 4+3 e imprimir el resultado.
No expliques nada.
Solo devuelve código.
"""

ARCHIVO_SALIDA = "programa_generado.py"
MAX_INTENTOS = 20
TIMEOUT_EJECUCION = 5

# ---------------------------------------------------
# GENERAR CÓDIGO CON OLLAMA
# ---------------------------------------------------

def generar_codigo():
    payload = {
        "model": MODELO,
        "prompt": PROMPT,
        "stream": False
    }

    respuesta = requests.post(URL, json=payload, timeout=60)
    respuesta.raise_for_status()

    texto = respuesta.json()["response"]

    # limpiar posible markdown
    texto = texto.replace("```python", "")
    texto = texto.replace("```", "")
    texto = texto.strip()

    return texto

# ---------------------------------------------------
# GUARDAR ARCHIVO
# ---------------------------------------------------

def guardar_codigo(codigo, ruta):
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(codigo)

# ---------------------------------------------------
# VALIDACIÓN ESTÁTICA
# ---------------------------------------------------

def validar_sintaxis(codigo):
    try:
        ast.parse(codigo)
        return True, "Sintaxis correcta"
    except SyntaxError as e:
        return False, f"Error de sintaxis: {e}"

def validar_seguridad_basica(codigo):
    """
    Validación simple para evitar instrucciones peligrosas.
    """
    palabras_prohibidas = [
        "os.system",
        "subprocess",
        "eval(",
        "exec(",
        "__import__",
        "open(",
        "requests",
        "socket",
        "shutil",
        "pathlib",
        "sys.exit",
        "quit(",
        "exit("
    ]

    codigo_minus = codigo.lower()
    for p in palabras_prohibidas:
        if p.lower() in codigo_minus:
            return False, f"Uso no permitido detectado: {p}"

    try:
        arbol = ast.parse(codigo)
    except SyntaxError as e:
        return False, f"Error de sintaxis: {e}"

    for nodo in ast.walk(arbol):
        if isinstance(nodo, (ast.Import, ast.ImportFrom)):
            return False, "No se permiten imports en el código generado"

    return True, "Validación de seguridad básica correcta"

# ---------------------------------------------------
# VALIDACIÓN FUNCIONAL
# ---------------------------------------------------

def validar_funcionamiento(ruta):
    try:
        resultado = subprocess.run(
            [sys.executable, ruta],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_EJECUCION
        )
    except subprocess.TimeoutExpired:
        return False, "Tiempo de ejecución agotado"

    if resultado.returncode != 0:
        return False, f"El programa falló al ejecutarse: {resultado.stderr.strip()}"

    salida = resultado.stdout.strip()

    if salida == "7":
        return True, "La salida es correcta"
    else:
        return False, f"Salida incorrecta: '{salida}'"

# ---------------------------------------------------
# VALIDACIÓN GLOBAL
# ---------------------------------------------------

def validar_codigo(codigo, ruta):
    ok, mensaje = validar_sintaxis(codigo)
    if not ok:
        return False, mensaje

    ok, mensaje = validar_seguridad_basica(codigo)
    if not ok:
        return False, mensaje

    guardar_codigo(codigo, ruta)

    ok, mensaje = validar_funcionamiento(ruta)
    if not ok:
        return False, mensaje

    return True, "Código válido"

# ---------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------

def main():
    print("🚀 Iniciando generación automática con validación...\n")

    for intento in range(1, MAX_INTENTOS + 1):
        print(f"Intento {intento}/{MAX_INTENTOS}")

        try:
            codigo = generar_codigo()
            es_valido, mensaje = validar_codigo(codigo, ARCHIVO_SALIDA)

            if es_valido:
                print("✅ Programa válido")
                print(f"📁 Archivo guardado: {ARCHIVO_SALIDA}")
                print("\nContenido final:\n")
                print(codigo)
                return
            else:
                print(f"❌ Programa no válido: {mensaje}\n")
                time.sleep(1)

        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión con Ollama: {e}\n")
            time.sleep(1)

        except Exception as e:
            print(f"❌ Error inesperado: {e}\n")
            time.sleep(1)

    print("❌ No se consiguió un programa válido tras varios intentos.")

if __name__ == "__main__":
    main()
