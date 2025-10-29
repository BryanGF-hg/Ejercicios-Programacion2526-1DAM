dividendo = 4
divisor = 0

try: 
 division = dividendo/divisor
except ZeroDivisionError:
 print("Tienes un error de division por cero")
except Exception as mierror:
 print("Hay un error")
 print(mierror)


########Puede que esten equivocados, comprobar manualmente(Solo es una prueba)########################
try:
    eval("x === 5")  # Error de sintaxis (solo se detecta al ejecutar con eval)
except SyntaxError as e:
    print("SyntaxError:", e)

try:
    print(variable_inexistente)
except NameError as e:
    print("NameError:", e)

try:
    print("hola" + 5)
except TypeError as e:
    print("TypeError:", e)

try:
    int("hola")
except ValueError as e:
    print("ValueError:", e)

try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError as e:
    print("IndexError:", e)

try:
    dic = {"a": 1}
    print(dic["b"])
except KeyError as e:
    print("KeyError:", e)

try:
    (5).hola
except AttributeError as e:
    print("AttributeError:", e)

try:
    print(5 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

try:
    import modulo_inexistente
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)

try:
    open("archivo_que_no_existe.txt")
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

try:
    assert 2 + 2 == 5
except AssertionError as e:
    print("AssertionError:", e)

# 🔹 Errores de aritmética
try:
    import math
    print(math.exp(1000))  # Desborde numérico
except OverflowError as e:
    print("OverflowError:", e)

