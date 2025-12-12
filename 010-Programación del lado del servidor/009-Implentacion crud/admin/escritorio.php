<!--http://..../basesdedatosdamdaw2526/008-Proyectos/003-Panel%20de%20control/101-Ejercicios/aplicacion/admin/escritorio.php -->

<!doctype html>
<html lang="es">
	<head>
  	<title>El jocarsa - Panel de control</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/estilos.css">
  </head>
  <body>
  	<nav>
    	<button>Noticias</button>
      <button>Autores</button>
    </nav>
    <main>
    	<?php
      	// Esto se conoce como router /////////////
      	if(isset($_GET['accion'])){
        	if($_GET['accion'] == "nuevo"){
          	include "inc/create/formulario.php";
          }else if($_GET['accion'] == "eliminar"){ // Defino la acción eliminar
          	include "inc/delete/eliminar.php";		// En ese caso incluyo eliminar.php
          }else if($_GET['accion'] == "editar"){
           include "inc/update/formularioactualizar.php";
          }
        }else{
       		include "inc/read/leer.php"; 
        }
      ?>
      <a href="?accion=nuevo" id="nuevo">+</a>    	
    </main>
  </body>
</html>
