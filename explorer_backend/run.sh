#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=explorer_backend.settings_test
deactivate >& /dev/null
source ht_env/bin/activate
python manage.py runserver
