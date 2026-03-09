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

MODELO = "deepseek-r1:1.5b"
URL = "http://localhost:11434/api/generate"

PROMPT = """
Genera únicamente código Python válido.

El programa debe:
- Implementar un CRUD de clientes en Python usando SQLite.
- Funcionar en consola.
- Crear una base de datos SQLite local.
- Incluir las operaciones: crear, listar, actualizar y borrar clientes.
- Tener una función main().
- Ser ejecutable directamente.
- Al arrancar, si no hay interacción del usuario, debe mostrar al menos un menú en consola y terminar correctamente si se elige salir.
- Usa únicamente librerías estándar de Python.
- No expliques nada.
- Solo devuelve código.
"""

ARCHIVO_SALIDA = "programa_generado.py"
MAX_INTENTOS = 20
TIMEOUT_EJECUCION = 5
TIMEOUT_CONEXION = 30  # Reducido de 60 a 30 segundos

# imports permitidos
IMPORTS_PERMITIDOS = {
    "sqlite3",
    "os",
    "sys"
}

# ---------------------------------------------------
# GENERAR CÓDIGO CON OLLAMA
# ---------------------------------------------------

def generar_codigo():
    payload = {
        "model": MODELO,
        "prompt": PROMPT,
        "stream": False
    }

    respuesta = requests.post(URL, json=payload)
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
        "eval(",
        "exec(",
        "compile(",
        "__import__",
        "open(",
        "os.system",
        "subprocess",
        "shutil",
        "socket",
        "requests",
        "urllib",
        "http",
        "ftplib",
        "telnetlib"
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
        if isinstance(nodo, ast.Import):
            for alias in nodo.names:
                nombre_base = alias.name.split(".")[0]
                if nombre_base not in IMPORTS_PERMITIDOS:
                    return False, f"Import no permitido: {nombre_base}"

        elif isinstance(nodo, ast.ImportFrom):
            if nodo.module is None:
                return False, "ImportFrom inválido"

            nombre_base = nodo.module.split(".")[0]
            if nombre_base not in IMPORTS_PERMITIDOS:
                return False, f"ImportFrom no permitido: {nombre_base}"

    return True, "Validación de seguridad básica correcta"

# ---------------------------------------------------
# VALIDACIÓN FUNCIONAL
# ---------------------------------------------------

def validar_funcionamiento(ruta):
    """
    Validación mínima para un CRUD:
    - el programa debe arrancar
    - no debe fallar inmediatamente
    - debe producir alguna salida
    """

    try:
        # Simulamos elegir salir inmediatamente con la opción 0
        resultado = subprocess.run(
            [sys.executable, ruta],
            input="0\n",
            capture_output=True,
            text=True,
            timeout=TIMEOUT_EJECUCION
        )
    except subprocess.TimeoutExpired:
        return False, "Tiempo de ejecución agotado"

    if resultado.returncode != 0:
        return False, f"El programa falló al ejecutarse: {resultado.stderr.strip()}"

    salida = resultado.stdout.strip().lower()

    if not salida:
        return False, "El programa no produjo salida"

    palabras_esperadas = ["cliente", "menu", "menú", "listar", "salir", "crud"]

    if any(p in salida for p in palabras_esperadas):
        return True, "El programa arranca y muestra una interfaz de consola válida"

    return False, f"Salida no reconocida como CRUD: '{resultado.stdout.strip()}'"

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
