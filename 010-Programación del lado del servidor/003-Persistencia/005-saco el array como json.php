<?php
  $cliente = [];
  $cliente['nombre'] = "Bryan";
  $cliente['apellidos'] = "Glot Fong";
  $cliente['email'] = "bryan@gmail.com";

  $json = json_encode($cliente);
  echo $json;    
?>
