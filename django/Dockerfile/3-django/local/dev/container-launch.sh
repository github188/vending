#!/usr/bin/env bash
python ../../proj/manage.py runserver 0.0.0.0:80 > /dev/null 2>&1 &
# python ../../proj/manage.py runmodwsgi --host 0.0.0.0 --port 80 --user mod_wsgi > /dev/null 2>&1 &