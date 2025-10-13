class CuentaBancaria():
 def __init__(self):
  self.__saldo = 0
  self.__cliente = ""
  
 # Defino setters y getters para el saldo
 def setSaldo(self,nuevosaldo):
  self.Saldo = nuevosaldo
 def getSaldo(self):
  return self.__saldo

cuentecliente1 = CuentaBancaria() 
cuentacliente1.setSaldo(10000000)
print(cuentacliente1.getSaldo()) 
