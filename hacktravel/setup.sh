#!/usr/bin/env bash

set -e

rm -rf ht_env > /dev/null
virtualenv -p python3.6 ht_env
source ht_env/bin/activate
pip install -r requirements.txt
./manage.py migrate
