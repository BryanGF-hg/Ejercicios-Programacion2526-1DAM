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
     <?php include "controladores/Leer.php"; ?>
    </main>
  </body>
</html>
