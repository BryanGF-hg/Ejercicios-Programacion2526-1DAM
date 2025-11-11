1.-Introducción:
Debemos crear una mini aplicación CRUD con la funcionalidad de crear clientes y listar clientes. Debemos hacer una clase cliente con propiedades, abrir el archivo binario con pickle, usar un bucle infinito que nos servirá de menú para crear clientes y listar cada cliente dentro del archivo

2.-Desarrollo:
Colocamos opcionalmente un título para el programa:
```
#Mini Aplicación CRUD -Create,Read,Update,Delete  
#Hecho por Bryan Glot Fong- 1 DAM
```

Importamos la libreria interna pickle que nos ayuda a leer, escribir, añadir información a archivos:
```
import pickle
```

Hacemos una clase cliente donde definimos un constructor y sus propiedades (nombre,apellidos,email):
```
class Cliente():
 def __init__(self):
  self.nombre = ""
  self.apellidos = ""
  self.email = ""
```


Creamos una lista vacía que nos servirá para guardar los clientes:
```
clientes = []
```


Hacemos una estructura de control de errores generales que nos servirá para abrir el archivo donde está guardada la información de la lista de clientes:
```
try:
 archivo = open("clientes.bin","rb")
 clientes = pickle.load(archivo)
 archivo.close()
except:
 print("Ha habido un error al abrir clientes.bin")
```


Creamos un bucle infinito controlado con el while:
```
while True:
```


Es importante que con pickle se escriba la información de los datos que el usuario ingresa cada vez que ocurra el bucle:
```
 archivo = open("clientes.bin","wb")
 pickle.dump(clientes,archivo)
 archivo.close()
```

Creamos decorativamente mensajes para que el usuario sepa que hacer en el programa:
```
 print("MENÚ"+"\n")
 print("1.-Crear clientes")
 print("2.-Leer clientes")
 print("3.-Salir del programa")
```

Hacemos una variable que nos permitirá movernos dentro de las opciones del menu que usaremos con futuros condicionales:
```
 opcion = int(input("Qué quieres hacer?"+"\n"))
```

Para la primera opción, le pedimos al usuario que nos de los datos de un nuevo cliente que se añadido a la lista:
```
 if opcion == 1:
  cliente = Cliente()
  cliente.nombre = input("Dame el nombre de un nuevo cliente:")
  cliente.apellidos = input("Dame los apellidos de un nuevo cliente:")
  cliente.email = input("Dame el email de un nuevo cliente:")
  clientes.append(cliente)
```


Para la segunda opción, creamos un identificador para usarlo en un bucle for por que nos permitirá leer los clientes que está dentro de la lista "clientes":
```
 elif opcion == 2:
  identificador = 0
  for cliente in clientes:
   print("Este es el cliente con ID:",identificador)
   print(cliente.nombre,cliente.apellidos,cliente.email)
   identificador += 1
```


Para la tercera opción, le permitimos al usuario salir del programa:
```
 elif opcion == 3:
  print("Ciao xiao")
  break
```


En cualquier caso que el programa no funcione creamos un else que nos permitirá saber si tiene un error el programa:
```
 else:
  break
```

3.-Aplicación:
Podemos aplicar el uso de una clase con propiedades y crear un bucle con diferentes menus usando una variables y en que cada menu tenga una funcionalidad diferente en muchos casos reales como guardado de información, registro de datos, historial de uso,etc.

4.-Conclusión:
Al crear una clase con propiedades, podemos crear entidades con diferentes utilidades y usarlos de una manera ética. Podemos crear comparaciones, registrar la información de esas propiedades para usarlas de una manera más avanzada, etc. También con el uso de bucles y estructuras tanto de control como de condicionales, crear programas que nos ayuden a hacer listas, tablas o conteos. Debemos tener en cuenta la perdida de datos que puede conllevar al usar la terminal de la máquina local y que los datos se pierdan, por ello, podemos llevar a cabo el uso de librerias que nos ayudaran a guardar la información en archivos o carpetas según lo requirido o cuanto el programa debe usarse.


Código:
```
#Mini Aplicación CRUD -Create,Read,Update,Delete  
#Hecho por Bryan Glot Fong- 1 DAM

import pickle
class Cliente():
 def __init__(self):
  self.nombre = ""
  self.apellidos = ""
  self.email = ""
  
clientes = []

try:
 archivo = open("clientes.bin","rb")
 clientes = pickle.load(archivo)
 archivo.close()
except:
 print("Ha habido un error al abrir clientes.bin")

print("Mini-aplicación de CRUD v0.1")
while True:
 archivo = open("clientes.bin","wb")
 pickle.dump(clientes,archivo)
 archivo.close()
 print("MENÚ"+"\n")
 print("1.-Crear clientes")
 print("2.-Leer clientes")
 print("3.-Salir del programa")
 
 opcion = int(input("Qué quieres hacer?"+"\n"))
 
 if opcion == 1:
  cliente = Cliente()
  cliente.nombre = input("Dame el nombre de un nuevo cliente:")
  cliente.apellidos = input("Dame los apellidos de un nuevo cliente:")
  cliente.email = input("Dame el email de un nuevo cliente:")
  clientes.append(cliente)
  
 elif opcion == 2:
  identificador = 0
  for cliente in clientes:
   print("Este es el cliente con ID:",identificador)
   print(cliente.nombre,cliente.apellidos,cliente.email)
   identificador += 1
   
 elif opcion == 3:
  print("Ciao xiao")
  break

 else:
  print("error")
```
