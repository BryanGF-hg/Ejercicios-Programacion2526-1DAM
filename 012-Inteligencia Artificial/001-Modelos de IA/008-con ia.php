<!doctype html>
<html>
	<head>
  	<style>
    	html,body{padding:0px;margin:0px;width:100%;height:100%;}
      body{display:flex;justify-content:center;align-items:center;}
      main{width:500px;height:500px;padding:20px;border:1px solid grey;
      border-radius:5px;display:flex;flex-direction:column;justify-content:space-between;}
      input{width:100%;padding:10px;box-sizing:border-box;}
      article{background:#FFD700;padding:20px;border-radius:10px 0px 10px 10px;}
    </style>
  </head>
  <body>
  	<main>
    	<section>
      	<article>
          <?php

          // sudo apt install php php-curl

          $OLLAMA_URL = "http://localhost:11434/api/generate";
          $MODEL = "qwen2.5:3b-instruct";

          $prompt = $_POST['mensaje'].".Responde en ESPAÑOL.
          
          
          Enfoque: Hacia las ramas de la informática, desarrollo multiplataforma, programación y lenguajes de marca
          Tono: neutral, directo, explicativo y si el usuario lo pide, permitir enrollarse y explicar a fondo en la cuestión,tema,resumen o activdad que se le pregunte.
          Visión global: Logre mejorar cada vez y registrar las connotaciones que uso con frecuencia
          Memoria de largo término: Que almacene la forma de escribir del usuario para que lo recuerde
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
          ?>        	
        </article>
      </section>
      <form action="?" method="POST">
      <input type="text" name="mensaje">
      </form>
    </main>
  </body>
</html>
