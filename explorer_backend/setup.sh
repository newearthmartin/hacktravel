#!/usr/bin/env bash
rm -rf ht_env > /dev/null
virtualenv -p python3.6 ht_env
source ht_env/bin/activate

echo Installing requirements...
pip install -q -r requirements.txt

echo Setting up DB...
./manage.py migrate
./manage.py createcachetable
deactivate
