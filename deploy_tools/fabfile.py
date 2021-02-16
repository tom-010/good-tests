import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run
import os

REPO_URL = 'https://github.com/tom-010/good-tests'

# export $(cat .env | xargs)  -- This one enables, that the .env file does
# not need to contain the exportkeywords, which would break systemd
# ./virtualenv/bin/python -- uses the python version of the installed
# virtualenv instead of the systemwiede python
manage_py = 'export $(cat .env | xargs) && ./virtualenv/bin/python manage.py'


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()
        _flush_database()
        #_add_cronjobs()
        _restart_service()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run(f'python3.6 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f"SITENAME={env.host}")
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghiklkmnopqrstuvwxyz01234567890', k=50))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files():
    run(f'{manage_py} collectstatic --noinput --clear')


def _update_database():
    run(f'{manage_py} migrate --no-input')


def _flush_database():
    if 'FLUSH_DATABASE' not in os.environ or not os.environ['FLUSH_DATABASE']:
        return
    run(f'{manage_py} flush --noinput')
    run(f'{manage_py} loaddata test_data.json')


def _add_cronjobs():
    try:
        run(f'{manage_py} crontab add')
    except Exception:
        # in case the job needs to be overwritten
        run(f'{manage_py} crontab add')


def _restart_service():
    run(f'./scripts/restart.sh {env.host}')
