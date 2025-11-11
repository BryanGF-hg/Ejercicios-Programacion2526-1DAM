1.-Introducción:
Queremos desarrollar una clase que tenga unas propiedades tanto para instanciarlas, es decir, usarlas para crear una entidad como para definir una propiedad y "colocar" una propiedad.

2.-Desarrollo:
Creamos una clase llamada Cliente:
```
class Cliente():
```

Creamos un constructor para hacer propiedades:
```
 def __init__(self):
```

Definimos las propiedades del cliente:
```
  self.nombre = "Usuario"
  self.apellidos = None
  self.email = ""
```

Creamos un método get que nos permite conseguir inmediamente la definición de la propiedad en vez de instanciarla y definirla:
```
 def getNombre(self):
  return self.nombre
```

Creamos un método set que nos permite cambiar la propiedad para usarla de otro modo:
```
 def setEmail(self,nuevoemail):
  self.email = nuevoemail
```

Instanciamos la clase tres veces y le ponemos sus propias propiedades:
```
cliente1 = Cliente()
cliente2 = Cliente()
cliente3 = Cliente()
```

Colocamos a las entidades sus propias propiedades de la clase:
```
cliente1.nombre = "Usuario1"
cliente1.apellidos = "Apellido del Usuario1"
cliente1.email = "usuario1@gmail.com"

cliente2.nombre = "Usuario2"
cliente2.apellidos = "Apellido del Usuario2"
cliente2.email = "usuario2@gmail.com"

cliente3.nombre = "Usuario3"
cliente3.apellidos = "Apellido del Usuario3"
cliente3.email = "usuario3@gmail.com"
```

Mostramos por pantalla las propiedades de la entidad:
```
print(cliente1.nombre,cliente1.apellidos,cliente1.email+"\n")
print(cliente2.nombre,cliente2.apellidos,cliente2.email+"\n")
print(cliente3.nombre,cliente3.apellidos,cliente3.email+"\n")
```

Usamos el método get según lo requerido:
```
cliente1 = Cliente()
print(cliente1.getNombre())
```

Hacemos lo mismo para el método set:
```
cliente1 = Cliente()
cliente1.setEmail("Cliente1 con un nuevo email")
```
3.-Aplicación:
Podemos aplicar una clase con propiedades para crear muchisimas entidades (personas,objetos,etc) en programas o aplicaciones donde debemos usar las mismas propiedades pero cada entidad tiene una diferentes que la permiten distinguir de otras.



4.-Conclusión:
Con el desarrollo de clases, nos permite crear propiedades que compartan varias entidades y poder distinguir de cada una. Podemos también registrarlas como datos y poder hacer una comparación de esos datos. También podemos extraer definiciones de las propiedades para poder usarla en una única entidad o en varias (es decir el método get), otro método que podemos usar el método set para colocar una propiedad en vez de definirla para el usuario o el uso que hagamos.



Código:
```
class Cliente():
 def __init__(self):
  self.nombre = "Usuario"
  self.apellidos = None
  self.email = ""
  
 def getNombre(self):
  return self.nombre

 def setEmail(self,nuevoemail):
  self.email = nuevoemail

cliente1 = Cliente()
cliente2 = Cliente()
cliente3 = Cliente()

cliente1.nombre = "Usuario1"
cliente1.apellidos = "Apellido del Usuario1"
cliente1.email = "usuario1@gmail.com"

cliente2.nombre = "Usuario2"
cliente2.apellidos = "Apellido del Usuario2"
cliente2.email = "usuario2@gmail.com"

cliente3.nombre = "Usuario3"
cliente3.apellidos = "Apellido del Usuario3"
cliente3.email = "usuario3@gmail.com"

print(cliente1.nombre,cliente1.apellidos,cliente1.email+"\n")
print(cliente2.nombre,cliente2.apellidos,cliente2.email+"\n")
print(cliente3.nombre,cliente3.apellidos,cliente3.email+"\n")

cliente1 = Cliente()
print(cliente1.getNombre())

cliente1 = Cliente()
cliente1.setEmail("Cliente1 con un nuevo email")
```
