<!doctype html>
<html>
	<head>
	  <meta charset type="utf-8">
	  <link rel="stylesheet" href="css/estilos.css">
 </head>
  <body>
    <?php include "inc/conexion_bbdd.php";?>
    <nav>
    <?php include "controladores/contenido_menu.php";?>
    </nav>
    <main>
   
     <?php
       //Enrutador: se encarga de manejar las operaciones a mostrar     
      if(!isset($_GET['operacion'])){    // Si no hay operacion
       include "controladores/Leer.php";
      }else{
        if($_GET['operacion'] == "insertar"){
         include "controladores/insertar.php";       
       }else if($_GET['operacion'] == "procesa_insertar"){
         include "controladores/procesa_insertar.php";
       }
      }
     ?>
     
     
    </main>
  </body>
</html>
