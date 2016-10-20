#!/usr/bin/env bash
sudo docker build -t omd-dev-local .
# docker network create --subnet 172.18.0.0/12 omd-dev-local

#dev run
sudo docker stop omd-dev-local
sudo docker rm -v omd-dev-local

sudo docker run -itd -v ~/Documents/git/github/vending:/volumeCode/vending \
-v ~/Documents/git/github/vending/django/Dockerfile/3-django/local/dev/mod_wsgi-express-80:/etc/mod_wsgi-express-80 \
--network omd-dev-local --ip 172.18.0.4 --name omd-dev-local --restart unless-stopped omd-dev-local bash