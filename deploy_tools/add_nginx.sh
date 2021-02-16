source .env

cat ./deploy_tools/nginx.template.conf \
| sed "s/DOMAIN/$SITENAME/g" \
| sed "s/USER/$USER/g" \
| sudo tee /etc/nginx/sites-available/$SITENAME

sudo ln -s /etc/nginx/sites-available/$SITENAME /etc/nginx/sites-enabled/$SITENAME

sudo systemctl daemon-reload
sudo systemctl reload nginx
