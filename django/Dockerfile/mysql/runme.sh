#!/usr/bin/env bash
#dev run
#sudo docker stop mysql-django
#sudo docker rm mysql-django

#-----if you want to map db to host filesystem
# if [ -e /mysql-django-vol ]; then rm -rf /mysql-django-vol; fi
#-----end

#sudo docker network create --driver bridge omd

#-------creating database dumps
#docker exec mysql-django sh -c 'exec mysqldump --all-databases -uroot -p"$"MYSQL_ROOT_PASSWORD"' > ~/Documents/mysql-django.sql
#-------backup database inside container
#mysqldump --all-databases -uroot -ppjsong > /etc/mysql/conf.d/backup.sql
#-------end

sudo docker run -d \
-v ~/Documents/git/github/vending/django/Dockerfile/mysql/conf.d:/etc/mysql/conf.d \
-v ~/Documents/git/github/vending/django/Dockerfile/mysql/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
--name mysql-django -e MYSQL_ROOT_PASSWORD=pjsong --restart unless-stopped -h mysql mysql

