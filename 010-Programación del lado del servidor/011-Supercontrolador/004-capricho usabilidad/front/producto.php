
<?php include "inc/cabecera.php"; ?>
<section id="pagina_producto">
  <?php
    $host = "localhost";
    $user = "tiendaonlinedamdaw";
    $pass = "Tiendaonlinedamdaw123$";
    $db   = "tiendaonlinedamdaw";

    $conexion = new mysqli($host, $user, $pass, $db);

    $sql = "SELECT * FROM producto WHERE id = ".$_GET['id'].";";

    $resultado = $conexion->query($sql);
    while ($fila = $resultado->fetch_assoc()) {
?>
	<article>
  	<div class="imagen"  style="background:url(img/producto.png);background-size:cover;"></div>
    <p><?= $fila['precio'] ?></p>
    <form action="carrito.php" method="POST">
       <input type="hidden" name="id" value="<?= $fila['id'] ?>">
       <input type="number" name="unidades" min=1 max=10 value=1>
       <input type="submit">
    </form>
 </article>
 <article>   
    <h3><?= $fila['nombre_producto'] ?></h3>
    <p><?= $fila['descripcion'] ?></p>
    <p><?= $fila['descripcion_larga'] ?></p>
  </article>
<?php
    }

    $conexion->close();
?>
</section>

<style>
 #pagina_producto{
  display:flex;
  gap:20px;
 }
 #pagina_producto article{
  text-align:center;
  flex:1;
 }
 #pagina_producto article .imagen{
  background:#90cdcd;
  height:100px;border-radius:5px 5px 0px 0px;
 }
 #pagina_producto article a{
  background:#7FFFEA;
  border-radius:5px;
  padding:10px;
  color:white;
  text-decoration:none;
 }
</style>
<?php include "inc/piedepagina.php"; ?>
