#INSTALACION
En linux:
sudo apt install git

O en Windows:
https://git-scm.com/install/windows

#git config --global user.name = "nombre"

#git config --global user.email = "email"

#Repositorio en servidor
Accedo a github para conseguir un repositorio:
https://github.com/jocarsa?tab=repositories
La url del repositorio que he creado es:
https://github.com/jocarsa/pruebadam2026

#Repositorio en local
1.-Navego hacia una carpeta (en vuestro caso puede ser la que queráis)
cd /var/www/html
2.-Ejecuto
git clone https://github.com/BryanGF-hg/practica-git-individual

(Estando en la carpeta del repositorio:)
cd practica-git-indivual/

#COMMIT:
git add prueba.txt
git commit -m "Mi primer commit"

Ahora creamos un nuevo archivo:
git add prueba2.txt
git commit -m "Este es mi segundo commit"

#TOKEN para hacer pull
git remote -v
Quitamos ssh:
git remote set-url origin https://github.com/jocarsa/pruebadam2026.git
git remote -v

josevicente@josevicenteportatil:/var/www/html/pruebadam2026$ git push origin main
Username for 'https://github.com': **En el usuario ponemos el usuario de GitHub**
Password for 'https://jocarsa@github.com': **En la contraseña ponemos el token que hemos generado**
Enumerando objetos: 7, listo.
Contando objetos: 100% (7/7), listo.
Compresión delta usando hasta 16 hilos
Comprimiendo objetos: 100% (4/4), listo.
Escribiendo objetos: 100% (6/6), 486 bytes | 486.00 KiB/s, listo.
Total 6 (delta 1), reusados 0 (delta 0), pack-reusados 0
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/jocarsa/pruebadam2026.git
   93dac3a..66cc286  main -> main
josevicente@josevicenteportatil:/var/www/html/pruebadam2026$
