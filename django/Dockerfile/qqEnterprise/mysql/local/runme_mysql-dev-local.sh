#!/usr/bin/env bash
#dev run
#sudo docker stop mysql-django
#sudo docker rm mysql-django

#-----if you want to map db to host filesystem
# if [ -e /mysql-django-vol ]; then rm -rf /mysql-django-vol; fi
#-----end

#sudo docker network create --driver bridge --subnet 172.18.0.0/16 omd-dev-local

#-------creating database dumps
#docker exec mysql-django sh -c 'exec mysqldump --all-databases -uroot -p"$"MYSQL_ROOT_PASSWORD"' > ~/Documents/mysql-django.sql
#-------backup database inside container
#mysqldump --all-databases -uroot -ppjsong > /etc/mysql/conf.d/backup.sql
#-------end

sudo docker run -d \
-v ~/Documents/git/github/vending/django/Dockerfile/qqEnterprise/mysql/conf.d:/etc/mysql/conf.d \
-v ~/Documents/git/github/vending/django/Dockerfile/qqEnterprise/mysql/local/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d \
--name mysql-qqEnterprise-local 0.0-e MYSQL_ROOT_PASSWORD=pjsong --restart unless-stopped \
--ip 172.18.0.11 --network omd-dev-local --network-alias mysql-qqEnterprise-local mysql-dev-local

