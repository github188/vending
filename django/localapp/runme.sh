#!/usr/bin/env bash
. ../ENV3/bin/activate
django-admin startproject root
cd root && python manage.py startapp webapp
python manage.py migrate
python manage.py makemigrations
#this is for update
python manage.py makemigrations blog
python manage.py sqlmigrate blog 0001
python manage.py createsuperuser