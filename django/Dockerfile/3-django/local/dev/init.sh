#!/usr/bin/env bash

# this file should be used when start a new project, with initial settings ready.
cd /volumeCode/vending/django;

#create localomd
django-admin startproject localomd
cd localomd
sed -i "/'django.contrib.staticfiles',/a\ \ \ \ 'mod_wsgi.server'," localomd/settings.py
sed -i "$ a STATIC_ROOT\ =\ os.path.join(BASE_DIR,\ 'static')" localomd/settings.py

# -------------------------https related configuration
#set me when behend a proxy; proxy strips this header from all incomming requests;
#proxy sets this header and sends to django  only for requests come in via https
# or let me unset
#sed -i "$ a SECURE_PROXY_SSL_HEADER\ =\ ('HTTP_X_FORWARDED_PROTO', 'https')" localomd/settings.py
#sed -i "$ a SESSION_COOKIE_SECURE\ =\ True" localomd/settings.py
#sed -i "$ a CSRF_COOKIE_SECURE\ =\ True" localomd/settings.py
#sed -i "$ a SESSION_EXPIRE_AT_BROWSER_CLOSE\ =\ True" localomd/settings.py
#sed -i "$ a os.environ['wsgi.url_scheme']\ =\ 'https'" localomd/settings.py
#sed -i '/os.environ.setdefault("DJANGO_SETTINGS_MODULE", "localomd.settings")/aos.environ["HTTPS"]\ =\ "on"' localomd/wsgi.py

# make use of SecurityMiddleware. redirects all non-HTTPS to HTTPS except for SECURE_REDIRECT_EXEMPT
#sed -i "$ a SECURE_SSL_REDIRECT\ =\ True" localomd/settings.py

sed -i 's/django.db.backends.sqlite3/django.db.backends.mysql/1' localomd/settings.py
sed -i "s/os.path.join(BASE_DIR, 'db.sqlite3')/'omd'/1" localomd/settings.py
sed -i "/'omd',/a\ \ \ \ 'USER': 'root'," localomd/settings.py
sed -i "/'USER': 'root',/a\ \ \ \ 'PASSWORD': 'pjsong'," localomd/settings.py
sed -i "/'PASSWORD': 'pjsong',/a\ \ \ \ 'HOST': 'mysql-omd-local'," localomd/settings.py

python manage.py makemigrations && python manage.py migrate \
&& python manage.py startapp localomddata && python manage.py startapp localomdweb \
&& python manage.py collectstatic --no-input

sed -i "/'django.contrib.staticfiles',/a\ \ \ \ 'localomddata'," localomd/settings.py
sed -i "/'django.contrib.staticfiles',/a\ \ \ \ 'localomdweb'," localomd/settings.py

#integration into mod_wsgi
# https://pypi.python.org/pypi/mod_wsgi
python manage.py runmodwsgi --setup-only --port=80 --user mod_wsgi --server-root=/volumeCode/vending/django/3-django/local/dev/mod_wsgi-express-80

#/volumeCode/vending/django/3-django/local/dev/mod_wsgi-express-80/apachectl start