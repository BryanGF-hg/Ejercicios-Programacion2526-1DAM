# 4 entre a produce un fallo de " entero entre cadena "

def hazDivision (dividendo,divisor):
  #Comprobamos si son números
 if isinstance(dividendo, (int,float,complex)) and isinstance(divisor, (int,float,complex)):
  #Comprobamos que el divisor no es cero
  if divisor != 0:
   resultado=dividendo/divisor
  else:
   resultado= 0
  return resultado
 else:
  return 0
 
print(hazDivision(4,"a"))

