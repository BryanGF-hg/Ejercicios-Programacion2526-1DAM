#Declaración y uso de constantes en Python
 
#Usando constantes nos permite almacenar unos valores que no cambian de lo cual podemos partir y usarlas tanto para operaciones o variables que cambiaran según las instrucciones del usuario

Primero definimos nuestras constantes en Mayúsculas:
```
DISTANCIA_CICLO= 40 
VELOCIDAD_MEDIA= 15 
```

Segundo, definimos la variable a usar en Minúsculas:
```
tiempo= DISTANCIA_CICLO /VELOCIDAD_MEDIA
```

Hacemos que la variable tiempo sea aproximada:
```
tiempo=round(tiempo)
```

Imprimimos los resultados de las constantes y variables en pantalla:
```
print("Has recorrido",DISTANCIA_CICLO,"con una velocidad media de ",VELOCIDAD_MEDIA, "con un tiempo de",tiempo)
```

La variable tiempo es muy importante en diferentes areas de la vida como las matemáticas, economía, arquitectura. Un ejemplo que podemos hacer es:
```
tiempo=input("Dame el tiempo de X actividad: ")
```
Que, en este caso, es una variable que podemos usar para hacer operaciones, almacenar un dato o otro fin.

Para concluir, es importante algunas veces usar constantes como en caso de usarlo fijamente como una cantidad específica de kilómetros en una carrera o la cantidad de recursos que usuaría en un viaje.




#Código:
```
DISTANCIA_CICLO= 40 
 -Distancia en km
VELOCIDAD_MEDIA= 15 
 -Velocidad en km/h
 

tiempo= DISTANCIA_CICLO /VELOCIDAD_MEDIA
tiempo=round(tiempo)

print("Has recorrido",DISTANCIA_CICLO,"con una velocidad media de ",VELOCIDAD_MEDIA, "con un tiempo de",tiempo)
```
