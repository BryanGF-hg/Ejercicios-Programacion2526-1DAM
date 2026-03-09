crontab -e

crontab -e

0 * * * * /usr/bin/python3 /var/www/html/generadorapuntesv3/apuntes.py "/var/www/html/dam/Segundo/Acceso a datos" >/dev/null 2>&1

0 * * * * = en el min 0 de cada hora de cada dia de cada dia de la semana de cada mes

* * * * *
│ │ │ │ │
│ │ │ │ └── día de la semana (0-7)
│ │ │ └──── mes (1-12)
│ │ └────── día del mes (1-31)
│ └──────── hora (0-23)
└────────── minuto (0-59)

A continuación el ejecutable

A continuación lo que quieres ejecutar

Donde está Python?
which python3

josevicente@josevicenteportatil:/var/www/html/programaciondam2526/012-Inteligencia Artificial/011-agente IA/101-Ejercicios$ whereis python3
python3: /usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/share/python3 /home/josevicente/.pyenv/shims/python3 /usr/share/man/man1/python3.1.gz
