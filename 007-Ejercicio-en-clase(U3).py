#Docstring
'''

'''

#Importaciones
#Este programa no requiere importaciones

#Declaraciones de variables globales
#Inicializamos las variables con valores vacíos

edad= 0
categoria= ""

#Funciones o clases
#En este programa no hay funciones o clases

#Función principal

edad= input("Introduce tu edad:")
edad= int(edad) #Convierto la edad en un entero
if edad<8:
 categoria= "pre-mini"
elif edad >= 8 and edad<=11:
 categoria= "mini"
elif edad >= 12 and edad<=15:
 categoria= "infantil"
elif edad >= 16 and edad<=17:
 categoria= "cadete"
elif edad >= 18 and edad<=20:
 categoria= "junior"
else:
 categoria= "senior"

print("Tu edad es de",edad,"años y tu categoria es:",categoria)

if edad > 40:
 print("Veterano con experiencia en la cancha")

