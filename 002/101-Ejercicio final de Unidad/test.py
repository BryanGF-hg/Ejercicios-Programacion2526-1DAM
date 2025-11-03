import random

numero_random = random.randint(0,50)
assert 1 <= numero_random <= 50

max_intento = 6
intento = 0

while  intento < max_intento:
 numero = input("Dame un número: ")
 try:
  numero = int(numero)
 except:
  print("error")
  continue                      #Entrada Invalida


 #Prueba de fuera de rango
 if numero<1 or numero>50:
  print("Fuera de rango")
  continue                      #Entrada Invalida

 intento = intento + 1
 assert intento >= 0

 if numero < numero_random:
  print("Demasiado bajo")
 elif numero > numero_random:
  print("Demasiado alto")
 elif numero == numero_random:
  break                         #Acierto
 else:
  print("error")
   
 if intento == 3:
  if numero_random%2 == 0:
   print("Pista: Número es PAR")
  else:
   print("Pista: Número es IMPAR")
   
if intento == max_intento or intento != max_intento:
 print("Has perdido. El número secreto era",numero_random)

