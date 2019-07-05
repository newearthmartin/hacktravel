#!/usr/bin/env bash
rm -rf ht_env > /dev/null
virtualenv -p python3.6 ht_env
source ht_env/bin/activate
pip install -r requirements.txt
./manage.py migrate
echo Creating superuser for admin. Enter password for admin user:
./manage.py createsuperuser --username admin --email martinmassera@gmail.com
