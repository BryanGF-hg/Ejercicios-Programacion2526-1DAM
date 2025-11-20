numeros = [1,2,"3",4,"cinco"]

print(numeros)

def calculaDoble():
 for numero in numeros:
  try:
    numero = int(numero)  # convierto en entero
    print(numero*2)
  except:
   print("(no valido)")
calculaDoble()
