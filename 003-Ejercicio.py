#Práctica de Entradas y Cambio de tipo de Dato

#Tipos de datos
La cantidad de variables utilizadas para convertirlas en otro tipo, es decir una cadena de texto a un número o un entero a un decimal resulta eficiente a niveles faciles como a niveles complejos.

Primero creamos una variable llamada edad_conductor para poder usarla según los requisitos pedidos:

```
edad_conductor=input("Dame la edad del conductor: ")
```

Luego convertimos esta variable a un entero en caso de introducir un número con decimal o como fracción:

```
edad_conductor=int(edad_conductor)
```

También calculamos una variable llamada doble para después mostrarla en pantalla:

```
doble=edad_conductor*2
```

Como resultado, mostramos en pantalla las dos variables calculadas:

```
print("La edad del conductor es: ",edad_conductor,"y el doble de su edad es: ",doble)
```

Algunas aplicaciones que podemos hacer de práctica son:

- Usar una función
```
variable=input()
```
para poder pedir una entrada al usuario para un fin a determinar

- Uso de una conversión de tipo de datos
```
variable=int()
```
Este es otra aplicación que podemos hacer cuando queramos convertir una variable de una manera específica.


Como conclusión, usando variables puede conllevar a que usemos unos tipos de datos no eficientes y a su vez, nos lleve a crear problemas o complicando números, por ejemplo. Por ello, se lleva a cabo la conversión de tipo de datos, ya sea por simplificación o por hacer que las variables sean más entendibles.





edad_conductor=input("Dame la edad del conductor: ")
edad_conductor=int(edad_conductor)

doble=edad_conductor*2

print("La edad del conductor es: ",edad_conductor,"y el doble de su edad es: ",doble)


