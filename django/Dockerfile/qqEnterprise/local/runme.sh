#!/usr/bin/env bash
PROJ_ROOT='~/Documents/git/github/vending/django/qqEnterprise'
ENV3_ROOT='~/Documents/git/github/vending/django/ENV3'

(cd $ENV3_ROOT) && source bin/activate && pip freeeze
(cd $PROJ_ROOT) && django-admin startproject qqEnterprise \
&& cd qqEnterprise && python manage.py makemigrations && python manage.py migrate

