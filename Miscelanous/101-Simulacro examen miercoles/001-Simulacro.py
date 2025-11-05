1.-Introducción:
Crearemos un programa de Python que nos permita conectar a nuestra base de datos, portafolio_simulacro, donde con un bucle infinito haremos un menu CRUD que permita al usuario crear, mostrar, actualizar y eliminar datos según lo requerido.

2.-Desarrollo:
Importamos la libreria interna de Python que nos permite conectarnos a la base de datos escrita en SQL:
```
import mysql.connector
```

Nos intentamos conectar a la base de datos usando la libreria mysql.connector y con el administrador, el usuario, la contraseña y la base de datos a utilizar:
```
conexion = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Contrasena123$",
    database="portafolio_simulacro"
)
```

Creamos varias impresiones para colocar un toque visual:
```
print("Bienvenido a una aplicación de Python con CRUD")
print("Uso de Base de Datos con las tablas [Pieza] y [Categoria]")
```

Recordemos crear un bucle infinito:
```
while True:
```

Mostramos visualmente al usuario que puede hacer con el programa:
```
 print("1.-Crear datos")
 print("2.-Mostrar datos")
 print("3.-Actualizar datos")
 print("4.-Eliminar datos")
```

Hacemos una variable que convertiremos a entero para que pueda funcionar el código futuro:
```
 opcion=int(input("Escoge una opción: "))
```

Para la primera opcion, debemos CREAR un cliente, es decir definir las variables que corresponden a las columnas que hemos hecho en la tabla Pieza:
```
 if opcion == 1:
   titulop =input("Introduce un título: ")
   descripcionp =input("Introduce una descripción: ")
   imagen =input("Introduce una imagen(texto): ")
   url =input("Introduce una url: ")
   id_categoria =input("Introduce una id categoría: ")
```

Luego intentamos hacemos conexion con la base de datos:
```
   cursor = conexion.cursor()
```

Ejecutamos el INGRESO en la tabla Pieza las variables que hemos introducidos en la pantalla:
```
   cursor.execute('''
     INSERT INTO Pieza
     VALUES(
     NULL,
     "'''+titulop+'''",
     "'''+descripcionp+'''",
     "'''+imagen+'''",
     "'''+url+'''",
     "'''+id_categoria+'''"
    );
    ''')
```

Y por ultimo exijimos la conexión:
```
   conexion.commit()
```

Para la segunda opción, LEER, nos conectamos a la conexión:
```
 elif opcion == 2:
   cursor = conexion.cursor()
```

Selecionamos la tabla para luego mostrala por pantalla:
```
   cursor.execute('''
    SELECT * FROM Pieza;
   ''')
  
Hacemos una variable que consiga todo la tabla y por cada fila que haya, muestre por pantalla las filas hecha:  
```
   filas = cursor.fetchall()

   for fila in filas:
    print(fila)
```

Exijimos la conexión y cerramos el intento de conexión:
```
   conexion.commit()
   cursor.close()
```

Para la tercera opción, ACTUALIZAR, debemos crear las variables que correspondan a la base de datos y el Identificador a actualizar:
```
 elif opcion == 3:
   Identificador = input("Introduce el Identificador a Actualizar: ")
   titulop =input("Introduce un título: ")
   descripcionp =input("Introduce una descripción: ")
   imagen =input("Introduce una imagen(texto): ")
   url =input("Introduce una url: ")
   id_categoria =input("Introduce una id categoría: ")
```

Hacemos un intento de conexión a la base de datos y ejecutamos el UPDATE para la tabla, SET para cambiar los valores y WHERE para el Identificador que hemos usado:
```
   cursor = conexion.cursor()
   cursor.execute('''
    UPDATE Pieza
    SET
    titulop = "'''+titulop+'''",
    descripcionp =  "'''+descripcionp+'''",
    imagen =  "'''+imagen+'''",
    url =  "'''+url+'''",
    id_categoria =  "'''+id_categoria+'''"
    WHERE Identificador =  "'''+Identificador+'''"
   ''')
```
Para la cuarta opción, ELIMINAR, hacemos un intento de conexión a la base de datos, luego creamos una variable identificador para eliminar toda la información que le corresponda:
```
 elif opcion == 4:
  cursor =conexion.cursor()
  identificador = input("Introduce el identificador a eliminar: ")

```

Ejecutamos el DELETE FROM para la tabla con WHERE usando la variable Identifcador que hemos creado:
```
  cursor.execute('''DELETE FROM Pieza WHERE Identificador= "'''+identificador+'''" ''')
```

Exijimos la conexión:
```
  conexion.commit()
```

Mostramos por pantalla que el identificador ha sido eliminado:
```
  print("El identificador",identificador,"ha sido eliminado")
```

Si ninguna de las opciones anteriores no funciona, haremos que el programa sea interruipdo:
```
 else:
  break
```

Cerramos la querida conexión:
```
conexion.close()
```

3.-Aplicación:
En un mundo donde los datos son importantes y es necesario aplicarlos de una manera eficente debemos usar el método CRUD es decir Crear, Leer, Actualizar y Eliminar para los datos. El uso de este programa puede ser usado en muchos ambitos donde requieran el uso de datos de manera frecuente o infrecuente.

4.-Conclusión:
Al crear un programa en un lenguaje de programación con una base de datos que está escrita en un lenguaje de bases de datos, podemos unirlas de manera que podamos crear, leer, actualizar y eliminar datos usando conceptos de programación al mismo tiempo de usar los datos de manera controlada. 

Código:
```
import mysql.connector

#Intentamos conexion a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="Admin",
    password="Contrasena123$",
    database="portafolio_simulacro"
)

print("Bienvenido a una aplicación de Python con CRUD")
print("Uso de Base de Datos con las tablas [Pieza] y [Categoria]")
while True:
 print("1.-Crear datos")
 print("2.-Mostrar datos")
 print("3.-Actualizar datos")
 print("4.-Eliminar datos")
 opcion=int(input("Escoge una opción: "))
 
 if opcion == 1:
   titulop =input("Introduce un título: ")
   descripcionp =input("Introduce una descripción: ")
   imagen =input("Introduce una imagen(texto): ")
   url =input("Introduce una url: ")
   id_categoria =input("Introduce una id categoría: ")
   
   #me conecto con la base de datos
   cursor = conexion.cursor()
   #Ejecutamos la introducción de las variables
   cursor.execute('''
     INSERT INTO Pieza
     VALUES(
     NULL,
     "'''+titulop+'''",
     "'''+descripcionp+'''",
     "'''+imagen+'''",
     "'''+url+'''",
     "'''+id_categoria+'''"
    );
    ''')
  #Intentamos hacer la conexión
   conexion.commit()
   
 elif opcion == 2:
   cursor = conexion.cursor()
   cursor.execute('''
    SELECT * FROM Pieza;
   ''')
  
   filas = cursor.fetchall()

   for fila in filas:
    print(fila)

   conexion.commit()
   cursor.close()
 elif opcion == 3:
   Identificador = input("Introduce el Identificador a Actualizar: ")
   titulop =input("Introduce un título: ")
   descripcionp =input("Introduce una descripción: ")
   imagen =input("Introduce una imagen(texto): ")
   url =input("Introduce una url: ")
   id_categoria =input("Introduce una id categoría: ")
   
   cursor = conexion.cursor()
   cursor.execute('''
    UPDATE Pieza
    SET
    titulop = "'''+titulop+'''",
    descripcionp =  "'''+descripcionp+'''",
    imagen =  "'''+imagen+'''",
    url =  "'''+url+'''",
    id_categoria =  "'''+id_categoria+'''"
    WHERE Identificador =  "'''+Identificador+'''"
   ''')
 elif opcion == 4:
  cursor =conexion.cursor()
  identificador = input("Introduce el identificador a eliminar: ")
  cursor.execute('''DELETE FROM Pieza WHERE Identificador= "'''+identificador+'''" ''')
  conexion.commit()
  print("El identificador",identificador,"ha sido eliminado")
 else:
  break

conexion.close()
```
