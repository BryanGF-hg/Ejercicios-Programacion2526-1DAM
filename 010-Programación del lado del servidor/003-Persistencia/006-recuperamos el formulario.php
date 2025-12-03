<!doctype html>
<html lang="es">
 <head>
  <meta charset type="utf-8">
  <style>
   body,html{width:100%;height:100%;padding:0px;margin:0px;}
body{display:flex;align-items:center;justify-content:center;background:#FFEAD2;flex-direction:column;}   
header,footer,main{background:white;width:400px;padding:20px;text-align:center;}
form{display:flex;flex-direction:column;gap:10px;} 
  </style>
 </head>
 <body>
  <header>
      <h1>preguntas y respuestas</h1>
  </header>
  <main>
   <form action=? method="POST">
    <label for="pregunta">Introduce tu pregunta</label>
    <input type="text" name="pregunta" id="pregunta">
    <label for="pregunta">Introduce la respuesta</label>
    <input type="text" name="respuesta" id="respuesta">    
    <input type="submit">
   </form>
  </main>
  <footer>
   <p>Finis</p>
<?php
  $json = json_encode($_POST); // Convierte POST a JSON
  echo $json;                  // Y lo saca por pantalla
?>
  </footer>
 </body>
</html>

