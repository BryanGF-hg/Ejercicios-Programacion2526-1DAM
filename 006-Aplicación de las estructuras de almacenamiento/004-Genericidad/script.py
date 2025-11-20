
from num2words import num2words

# Generar lista de los 200 primeros números en palabras (0 a 199)
numeros_etiquetas = [num2words(i, lang='es') for i in range(200)]

# Mostrar la lista completa
for palabra in numeros_etiquetas:
    print(palabra)

