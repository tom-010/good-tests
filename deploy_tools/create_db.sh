if [ -z "$1" ]
then
      echo "Please provide a database name"
      exit 1
fi

database=$1
user=$database
password=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 40 ; echo '')

create_user_command="
create user $user with encrypted password '$password';
alter user $user with superuser;"

create_db_command="
create database $database;"

grant_persmissions_command="
grant all on database $database to $user;"


echo "creating database"
sudo -u postgres -H -- psql -c "$create_user_command" || exit 1

echo "creating user"
sudo -u postgres -H -- psql -c "$create_db_command" || exit 1

echo "granting permissions"
sudo -u postgres -H -- psql -c "$grant_persmissions_command" || exit 1

echo "DB_NAME=$database" >> .env
echo "DB_PASSWORD=$password" >> .env
echo "added to ./.env"