#!/usr/bin/env bash
#python ../../proj/manage.py runserver 0.0.0.0:80 > /dev/null 2>&1 &
# python ../../proj/manage.py runmodwsgi --host 0.0.0.0 --port 80 --user mod_wsgi > /dev/null 2>&1 &

# integration into mod_wsgi
# https://pypi.python.org/pypi/mod_wsgi
python ../../../../localomd/manage.py runmodwsgi --setup-only \
--port=80 --https-only --https-port=443 \
#--document-root=mod_wsgi-express-80
--allow-localhost
--ssl-certificate-file=./ssl/omd-dev-local.crt \
--ssl-certificate-key-file=./ssl/omd-dev-local.key \
--server-name=localomd.oursmedia.cn \
--user mod_wsgi \
--server-root=/volumeCode/vending/django/Dockerfile/3-django/local/dev/mod_wsgi-express-80

/volumeCode/vending/django/Dockerfile/3-django/local/dev/mod_wsgi-express-80/apachectl start