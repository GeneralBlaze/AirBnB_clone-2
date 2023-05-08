#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files
sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
content='<!DOCTYPE html>
<html lang="en">
        <head>
                <title>Fake website</title>
        </head>
        <body>Just testing</body>
</html>'
echo "$content" > /data/web_static/releases/test/index.html
sudo chown -hR ubuntu:ubuntu /data/
config="server {
        listen 80 default_server;
        listen [::]:80 default_server;
        location /hbnb_static {
                alias /data/web_static/current;
        }
}"

echo -e "$config" > /etc/nginx/sites-enabled/default
sudo service nginx restart
