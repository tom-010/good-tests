# 1. run backup on live system
ssh pring2me@5.45.106.120 'cd ~/sites/good-tests.com && ./scripts/backup.sh'
# 2. scp it down
scp pring2me@5.45.106.120:~/sites/good-tests.com/backups/latest.json ./latest.json
# 3. sync down media 
rsync -av --delete -e ssh pring2me@5.45.106.120:~/sites/good-tests.com/media/images ./media
# 4. clean the db to enable playing it in
python3 scripts/clean.py
# 5. flush current db
python3 manage.py flush --no-input
# 6. load the data
python3 manage.py loaddata latest.json
# 7. clean up
rm latest.json
# 8. change superuser
python3 manage.py changepassword admin