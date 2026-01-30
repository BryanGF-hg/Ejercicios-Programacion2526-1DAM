<?php

// sudo apt install php php-curl
// sudo service apache2 restart

$OLLAMA_URL = "http://localhost:11434/api/generate";
$MODEL = "qwen2.5:3b-instruct";

$prompt = "Sanea la siguiente cadena, 
	- pon comas, 
  - puntos, 
  - separa en frases,
	- y si es necesario, separa en párrafos si existen diferentes temas. 
  
  -Devuelve frases y párrafos en HTML, pon <br> al final de cada linea, y doble <br> al final de cada parrafo
  -Detecta las cuatro palabras mas importantes de cada parrafo, y ponlas en negrita 
  -Pon en mayúsculas la primera letra de cada frase o párrafo
   
  
  La cadena es:
para ello voy a hacer un ejercicio que suele ser divertido que es el siguiente vamos a ver voy a copiar Esto vale esto lo voy a guardar como dibujo animado Vale entonces digo While true W un eh vamos a ver voy a decir print Hola pero quiero import Time y quiero Time slip f5 Vale y vemos que cada segundo o sea se espera la ejecución se espera un segundo entro en un bucle infinito pero es un bucle infinito controlado Por cierto que más adelante cuando hablemos de bucles infinitos también estaré hablando de la estructura de control Tri Catch que lo que hace es en un momento dado Escuchar una tecla para poder parar el bucle de momento voy a pulsar control c es decir lo paro a la Ob bestia en este caso vamos a ver voy a cerrar esto voy a pulsar f5 vale vemos que hasta que no acaba el bucle no hace el Lienzo punto pack Esto me puede llegar a fastidiar vamos a ver porque yo lo que quiero es esto vamos a ver Lienzo Canvas esto lo quiero aquí pulso f5 Ah Sí perdón este indent va aquí vale Y hasta que no paro claro no crea es que esto lo que ha hecho es crear un montón de elementos uno dentro del otro vale voy a hacer una cosa voy a pasar a lo del tema de la imagen y ahora volvemos a este archivo pero como te puedes imaginar lo que quiero es un archivo que lo que haga es que vaya dibujando poco a poco un elemento no borrar todavía no quiero borrar el canvas pero sí por lo menos que vaya dibujando progresivamente Pues un círculo de forma aleatoria en pantalla vamos de momento a hablar de el tema de dibujar imagen entonces voy a crear un nuevo archivo
  ";

$data = [
    "model" => $MODEL,
    "prompt" => $prompt,
    "stream" => false
];

$ch = curl_init($OLLAMA_URL);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json"
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

$response = curl_exec($ch);

if ($response === false) {
    die("cURL error: " . curl_error($ch));
}

curl_close($ch);

$result = json_decode($response, true);

echo $result["response"];

