class Matematicas():
 def __init__(self):
  self.numero = 0
 #Hacemos el metodo de abajo que sea estático
 @staticmethod
 def suma(a,b):
  #a y b son parámetros
  return a+b
  
print(Matematicas.suma(6,7))



