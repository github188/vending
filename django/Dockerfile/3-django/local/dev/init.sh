#!/usr/bin/env bash

# this file should be used when start a new project, with initial settings ready.
cd /volumeCode/vending/django;

#create localomd
django-admin startproject localomd
cd localomd
sed -i "/'django.contrib.staticfiles',/a\ \ \ \ 'mod_wsgi.server'," localomd/settings.py
sed -i "$ a STATIC_ROOT\ =\ os.path.join(BASE_DIR,\ 'static')" localomd/settings.py

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
