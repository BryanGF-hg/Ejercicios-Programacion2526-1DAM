Finalizamos conectando gunicorn con NGINX:

sudo nano /etc/nginx/sites-available/miweb

Con nano ponemos esto:

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}


sudo ln -s /etc/nginx/sites-available/miweb /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

Y reiniciamos:
sudo systemctl restart nginx
sudo systemctl status nginx

