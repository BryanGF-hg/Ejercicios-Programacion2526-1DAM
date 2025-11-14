#Uso de literales y variables

Los literales o variables constantes (hasta que se encuentre una función que cambie su valor) no son tan importantes por el hecho de encontrarnos con problemas que cambian de estado. Es importante en el Virtual Streaming y como en cualquier otra area de la vida, el uso de variables ya sea por causas internas o externas.

Primero definimos dos literales:
```
nombre_vtuber="Mint"
edad=19
```

Luego le pedimos al usuario que cambie el valor de las dos variables: 
```
nombre_vtuber=input("Dame el nombre de una vtuber: ")
edad=input("Dame tu edad: ")
```


Luego mostramos por pantalla las dos variables que hemos cambiado:
```
print("Esta es la vtuber que has mencionado: ",nombre_vtuber,"y esta es tu edad: ",edad)
```

En conclusión, los literales son importantes cuando queremos que algunos valores queden registrados en el programa para una causa de forma cerrada.


nombre_vtuber="Mint"
edad=19

nombre_vtuber=input("Dame el nombre de una vtuber: ")
edad=input("Dame tu edad: ")

nombre_vtuber=str(nombre_vtuber)
edad=int(edad)

print("Esta es la vtuber que has mencionado: ",nombre_vtuber,"y esta es tu edad: ",edad)

