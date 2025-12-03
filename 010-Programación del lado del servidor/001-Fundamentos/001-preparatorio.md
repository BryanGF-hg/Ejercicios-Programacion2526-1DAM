PHP es un lenguaje del lado del servidor
Requiere que tengamos un seridor preparado

Formas fáciles de preparar un servidor

En linux(la buena):
Terminal:
sudo apt install apache2 (instalar apache)
sudo apt install php (para instalar php sobre apache)
sudo chdmod 777 -R /var/www/html (para dar permisos a la carpeta)

Y a partir de ese momento:
1.- Todos los archivos se meten dentro de var/www/html
2.- En navegador ponemos http://localhost/...

En Windows (la forma mala):
1.- Descargamos XAMPP: https://www.apachefriends.org/es/index.html
2.- Instalamos XAMPP
En el panel de control de XAMPP arrancamos de momento solo apache

Y a partir de ese momento:
1.-Todos los archivos se meten dentro de C:/xampp/htdocs
2.-En el navegador ponemos http://localhost/....
