git remote -v

Quitamos ssh:
git remote set-url origin https://github.com/jocarsa/pruebadam2026.git
git remote -v

josevicente@josevicenteportatil:/var/www/html/pruebadam2026$ git push origin main
Username for 'https://github.com': jocarsa
Password for 'https://jocarsa@github.com': 
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

Hacemos push
En el usuario ponemos el usuario de GitHub
En la contraseña ponemos el token que hemos generado



