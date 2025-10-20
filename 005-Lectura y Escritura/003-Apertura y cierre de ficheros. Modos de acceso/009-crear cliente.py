class Cliente():
 def __init__ (self,nuevonombre,nuevoemail):
  self.nombre = nuevonombre
  self.email = nuevoemail
  
clientes = []

clientes.append(Cliente("Bryan Glot Fong","info@gmail.com"))
clientes.append(Cliente("Ibrahim Glot Fong","info1@gmail.com"))

print(clientes)
