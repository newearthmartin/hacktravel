#!/usr/bin/env bash
deactivate >& /dev/null
source ht_env/bin/activate
python manage.py runserver