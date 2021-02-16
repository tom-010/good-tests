source .env
./deploy_tools/add_systemd.sh
./deploy_tools/add_nginx.sh
./deploy_tools/add_ssl_certificate.sh
DB_NAME=${SITENAME//\./_}
./deploy_tools/create_db.sh $DB_NAME