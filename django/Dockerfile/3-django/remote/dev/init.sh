#!/usr/bin/env bash

# this file should be used when start a new project, with initial settings ready.
cd /volumeCode/vending/django;

#create remoteomd
django-admin startproject remoteomd
cd remoteomd
sed -i "/'django.contrib.staticfiles',/a\ \ \ \ 'mod_wsgi.server'," proj/settings.py
sed -i "$ a STATIC_ROOT\ =\ os.path.join(BASE_DIR,\ 'static')" proj/settings.py

sed -i 's/django.db.backends.sqlite3/django.db.backends.mysql/1' proj/settings.py
sed -i "s/os.path.join(BASE_DIR, 'db.sqlite3')/'omd'/1" proj/settings.py
sed -i "/'omd',/a\ \ \ \ 'USER': 'root'," proj/settings.py
sed -i "/'USER': 'root',/a\ \ \ \ 'PASSWORD': 'pjsong'," proj/settings.py
sed -i "/'PASSWORD': 'pjsong',/a\ \ \ \ 'HOST': 'mysql-omd-remote'," proj/settings.py

python manage.py makemigrations && python manage.py migrate \
&& python manage.py startapp remoteomddata && python manage.py startapp remoteomdweb \
&& python manage.py collectstatic --no-input

sed -i "/'django.contrib.staticfiles',/a\ \ \ \ 'remoteomddata'," proj/settings.py
sed -i "/'django.contrib.staticfiles',/a\ \ \ \ 'remoteomdweb'," proj/settings.py
