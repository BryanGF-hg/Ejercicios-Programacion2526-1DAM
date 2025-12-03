<?php
 class Arma{
  function __construct($color,$mira){
    $this->color = $color;
    $this->mira = $mira;
  }
 }
 
 $arma1 = new Arma("KAR98K","Sniper Scope");
 $arma2 = new Arma("COLTM1911","Sin Scope");
 
 var_dump($arma1);
 var_dump($arma2);
?>
