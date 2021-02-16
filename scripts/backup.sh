NAME=$(date +%Y-%m-%d_%H-%M-%S)
mkdir backups 2> /dev/null
NAME="$NAME.sql"
export $(cat .env | xargs) && ./virtualenv/bin/python3 manage.py dumpdata > backups/latest.json
cp backups/latest.json backups/$NAME