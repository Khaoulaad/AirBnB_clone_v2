#!/usr/bin/env bash
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Output directory contents for debugging
ls -la /data/web_static/releases/test

# Create symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Output symbolic link information for debugging
ls -la /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Output ownership information for debugging
ls -la /data

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static/ {n; n; n; n; n; n; n; n; s/#/ /}' $nginx_config
sudo sed -i '/location \/hbnb_static/ {n; n; n; n; n; n; s/#/ /}' $nginx_config

# Restart Nginx
sudo service nginx restart
