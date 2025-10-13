'''
Aplicación de gestión de productos
Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

#Definimos clases y funciones
class Product():
 def __init__(self):
  self.nombre = ""
  self.precio = 0

#Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1")
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción: ")
print("1.-Crear un nuevo producto")
print("2.-listar productos")
print("3.-actualizar productos ")
print("4.-Eliminar productos")
opcion = int(input("Escoge tu opción: "))
# En función de la opción que coja el usuario

 # O bien creamos un nuevo producto
 # O bien listamos los productos
 # O bien actualizamos los productos 
 # O bien eliminamos los productos
# Y volvemos a repetir


