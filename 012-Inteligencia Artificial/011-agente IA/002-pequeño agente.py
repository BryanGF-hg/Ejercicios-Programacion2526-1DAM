#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# ---------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------

MODELO = "deepseek-r1:1.5b"   # o llama3, mistral, etc.
URL = "http://localhost:11434/api/generate"

PROMPT = """
Genera únicamente código Python válido.
El programa debe sumar 4+3 e imprimir el resultado.
No expliques nada.
Solo devuelve código.
"""

ARCHIVO_SALIDA = "programa_generado.py"

# ---------------------------------------------------
# PETICIÓN A OLLAMA
# ---------------------------------------------------

payload = {
    "model": MODELO,
    "prompt": PROMPT,
    "stream": False
}

respuesta = requests.post(URL, json=payload)

# ---------------------------------------------------
# PROCESAR RESPUESTA
# ---------------------------------------------------

if respuesta.status_code == 200:
    texto = respuesta.json()["response"]

    # limpiar posible markdown
    texto = texto.replace("```python", "")
    texto = texto.replace("```", "")
    texto = texto.strip()

    # guardar archivo
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        f.write(texto)

    print("✅ Archivo guardado:", ARCHIVO_SALIDA)
    print("\nContenido generado:\n")
    print(texto)

else:
    print("❌ Error:", respuesta.status_code)
    print(respuesta.text)
