kill -HUP $(pgrep -d " " -f gunicorn.*$1)
exit 0