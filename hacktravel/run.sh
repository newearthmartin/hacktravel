#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=hacktravel.settings
deactivate >& /dev/null
source ht_env/bin/activate
python manage.py runserver