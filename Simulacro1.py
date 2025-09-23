
```
 Programa de cambio de tipo de datos 

Este programa nos permitirá cambiar unas variables literales (creadas por el usuario) a cualquier valor que queramos. Esto nos permite hacer unos cambios más complejos cuando lleguemos a crear programas que requieran multiples variables a modificar.


Primero definimos nuestras variables, "videojuego" y "puntuacion" con un valor constante. Luego le pediremos al usuario que nos de, al primer valor, una cadena de texto y al segundo, un número entero.
Creamos otra variable que nos pide las tareas, "doble" según lo pedido:

doble = puntuacion*2

 y después usaremos para el resultado final en el cual se muestra en pantalla:

print("Tu videojuego favorito es,"+videojuego, "y su puntuación doble de",+doble)


Algunos errores que podemos encontrar son como olvidar el uso de conversiones de tipo (cadena de texto a numero) o el caso de no colocar el signo "+" con una variable dentro de la función "print()"

En conclusión, al modificar variables con un dato específico para luego ser usadas de otra manera es decir, primero como una cadena de texto y después un número entero resulta útil tanto a nivel sencillo como a nivel complejo
```

videojuego = 0
puntuacion = 0

videojuego = input("Dame el nombre de tu videojuego favorito:")
puntuacion = int(input("Dame la puntuacion de tu videojuego favorito del 1 al 10:"))

doble = puntuacion*2

print("Tu videojuego favorito es,"+videojuego, "y su puntuación doble de",+doble)










