source .env

cat ./deploy_tools/gunicorn-systemd.template.service \
| sed "s/DOMAIN/$SITENAME/g" \
| sed "s/USER/$USER/g" \
| sudo tee /etc/systemd/system/gunicorn-$SITENAME.service

sudo systemctl daemon-reload
sudo systemctl enable gunicorn-$SITENAME
sudo systemctl start gunicorn-$SITENAME