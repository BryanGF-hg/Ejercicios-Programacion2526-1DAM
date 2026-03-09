#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
import subprocess
import sys
import time
import requests

# ---------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------

MODELO = "deepseek-r1:1.5b"
URL = "http://localhost:11434/api/generate"

ARCHIVO_SALIDA = "programa_generado.py"
MAX_INTENTOS = 5
TIMEOUT_EJECUCION = 5
MAX_ERRORES_MEMORIA = 5

IMPORTS_PERMITIDOS = {
    "sqlite3",
    "os",
    "sys"
}

PROMPT_BASE = """
Genera únicamente código Python válido.

Crea un programa de consola en Python usando SQLite que implemente un CRUD de clientes.

Requisitos:
- Usa sqlite3
- Base de datos SQLite local
- Tabla clientes si no existe
- Campos: id, nombre, email, telefono
- Operaciones: crear, listar, actualizar, borrar
- Debe tener una función main()
- Debe incluir: if __name__ == "__main__": main()
- Usa solo librerías estándar
- No expliques nada
- Solo devuelve código

MUY IMPORTANTE:
- El programa será ejecutado automáticamente en un entorno no interactivo
- No debe fallar si no hay entrada disponible por teclado
- Si usas input(), debes controlar EOFError
- Si no hay entrada, el programa debe terminar limpiamente
- No generes un programa que dependa obligatoriamente de interacción humana real
"""

# ---------------------------------------------------
# MEMORIA DE ERRORES
# ---------------------------------------------------

memoria_errores = []

def construir_prompt():
    prompt = PROMPT_BASE.strip()

    if memoria_errores:
        prompt += "\n\nERRORES PREVIOS QUE NO DEBES REPETIR:\n"
        for i, err in enumerate(memoria_errores[-MAX_ERRORES_MEMORIA:], 1):
            prompt += f"{i}. {err}\n"

    prompt += """
DEVUELVE SOLO CÓDIGO PYTHON.
NO USES BLOQUES MARKDOWN.
"""
    return prompt

def registrar_error(mensaje):
    mensaje = mensaje.strip()
    if mensaje and mensaje not in memoria_errores:
        memoria_errores.append(mensaje)

# ---------------------------------------------------
# GENERAR CÓDIGO CON OLLAMA
# ---------------------------------------------------

def generar_codigo():
    prompt = construir_prompt()

    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    }

    respuesta = requests.post(URL, json=payload)
    respuesta.raise_for_status()

    texto = respuesta.json()["response"]

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
    palabras_prohibidas = [
        "eval(",
        "exec(",
        "compile(",
        "__import__",
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
# DETECCIÓN DE ERRORES REPETIDOS
# ---------------------------------------------------

def analizar_error_para_memoria(mensaje_error):
    texto = mensaje_error.lower()

    if "eoferror" in texto:
        return "No uses input() sin controlar EOFError. El programa debe funcionar también sin entrada interactiva."

    if "timeout" in texto or "tiempo de ejecución agotado" in texto:
        return "No generes un programa que se quede esperando indefinidamente. Debe terminar rápido."

    if "import no permitido" in texto:
        return "Usa únicamente imports permitidos y librerías estándar autorizadas."

    if "syntaxerror" in texto or "error de sintaxis" in texto:
        return "El código debe tener sintaxis Python completamente válida."

    if "no produjo salida" in texto:
        return "El programa debe imprimir algo útil en consola al arrancar."

    if "sqlite" in texto and "error" in texto:
        return "El acceso a SQLite debe funcionar correctamente y crear la tabla si no existe."

    return f"No repitas este error: {mensaje_error}"

# ---------------------------------------------------
# VALIDACIÓN FUNCIONAL
# ---------------------------------------------------

def validar_funcionamiento(ruta):
    try:
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
        stderr = resultado.stderr.strip()
        stdout = resultado.stdout.strip()

        detalle = stderr if stderr else stdout
        return False, f"El programa falló al ejecutarse: {detalle}"

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
    print("🚀 Iniciando generación automática con validación y memoria...\n")

    for intento in range(1, MAX_INTENTOS + 1):
        print(f"Intento {intento}/{MAX_INTENTOS}")

        if memoria_errores:
            print("🧠 Memoria de errores acumulada:")
            for i, err in enumerate(memoria_errores[-MAX_ERRORES_MEMORIA:], 1):
                print(f"   {i}. {err}")
            print()

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
                registrar_error(analizar_error_para_memoria(mensaje))
                time.sleep(1)

        except requests.exceptions.RequestException as e:
            msg = f"Error de conexión con Ollama: {e}"
            print(f"❌ {msg}\n")
            registrar_error("La respuesta del modelo o la conexión falló. Genera código de forma más breve y directa.")
            time.sleep(1)

        except Exception as e:
            msg = f"Error inesperado: {e}"
            print(f"❌ {msg}\n")
            registrar_error(f"No repitas este error inesperado: {e}")
            time.sleep(1)

    print("❌ No se consiguió un programa válido tras varios intentos.")

if __name__ == "__main__":
    main()
