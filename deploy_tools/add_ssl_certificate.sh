source .env

num=$(echo "${SITENAME}" | awk -F. '{print NF-1}')

if [ "${num}" -gt 1 ] # it is subdomain with more than one dot
then
    sudo certbot --nginx -d $SITENAME
else
    sudo certbot --nginx -d $SITENAME -d "www.${SITENAME}"
fi

sudo systemctl daemon-reload
sudo systemctl reload nginx
