'''
    Calculadora de cuadras
    v0.1
    Programa que calcula número de cuadras a partir de los caballos
'''

import math as matematicas
# Datos de Inicio
caballos= 0
cuadras = 0
caballos_por_cuadra = 0

# Entrada de información
caballos_por_cuadra= int(input("Introduce el número de caballos por cuadra: "))
caballos= int(input("Introduce el número de caballos: "))
cuadras = caballos/caballos_por_cuadra
redondeo = matematicas.ceil(cuadras)

#Salidas de resultados
print("Si tienes",caballos,"caballos")
print("Y te caben tres caballos por cuadra")
print("En ese caso necesitas",redondeo,"cuadras")






