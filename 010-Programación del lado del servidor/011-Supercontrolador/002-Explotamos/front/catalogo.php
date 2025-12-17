
<?php include "inc/cabecera.php"; ?>
<section id="catalogo">
  <?php
    $host = "localhost";
    $user = "tiendaonlinedamdaw";
    $pass = "Tiendaonlinedamdaw123$";
    $db   = "tiendaonlinedamdaw";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM producto;";

    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {
?>
	<article>
  	<div class="imagen" style="background:url(img/producto.png);background-size:cover;"></div>
    <h3><?= $fila['nombre_producto'] ?></h3>
    <p><?= $fila['precio'] ?></p>
    <p><?= $fila['descripcion'] ?></p>
    <a href="producto.php?id=<?= $fila['id'] ?>">Comprar</a>           <!-- IMportante -->
  </article>
<?php
    }

    $conexion->close();
?>
</section>

<style>
 #catalogo{
  display:grid;
  grid-template-columns: repeat(4, 1fr);
  gap:20px;
 }
 #catalogo article{
  text-align:center;
 }
 #catalogo .imagen{
  background:#4799a5;
  height:100px;border-radius:5px 5px 0px 0px;
 }
 #catalogo article a{
  background:#4799a5;
  border-radius:5px;
  padding:10px;
  color:white;
  text-decoration:none;
 }
</style>
<?php include "inc/piedepagina.php"; ?>
