php.ini en Windows:
C:/xampp/php/php.ini
(Espero que no sea vuestro caso)

En Ubuntu está en:
/etc/php/8.3/apache2/php.ini

Si no os deja modificar con gedit

sudo nano /etc/php/8.3/apache2/php.ini

Comandos:
(Parece que si que deja hacer scroll)
Control + W = Buscar (where)
Control + O = Guardar
Control + X = Salir
Teneis la ayuda bajo del editor

display_errors = Off (Cambiar de Off a On)

Cuado se toca el php.ini hay que reiniciar apache

sudo service apache2 restart
(para aplicar los cambios)
