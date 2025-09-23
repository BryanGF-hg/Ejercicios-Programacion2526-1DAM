#Programa con un uso de bucles for
#Conteo de patitos de goma en una fábrica

'''
Los años de producción (del 2000 al 2025)
Los meses del año (del 1 al 12)
Los días del mes (del 1 al 30)
'''

#Por cada día, el programa mostrará un mensaje indicando cuanto patitos de goma se han fabricado ese día

#Requisitos Adicionales:
'''
    1.Cada día se fabrican exactamente 10 patitos de goma
    2.El programa debe mostrar mensajes como:

Día 5 del mes 3 del año 2010: 10 patitos de goma fabricados

    3.Al terminar el bucle, el programa debe mostrar el total de patitos fabricados en todo el periodo

Algunos errores que podemos encontrar son como olvidar dejar espacio para relacionar la variable (?)

'''

patitos=10
anio=1
meses=1
dia=1

for anio in range(2000,2026):
 for meses in range(1,13):
  for dia in range(1,31):
   print("Día",dia,"del mes",meses,"del año",anio,":",patitos, "patitos de goma fabricados")
   patitos += 10







