#!/usr/bin/env bash
#sudo docker build -t django-omd .

#prod run
#sudo docker run -d --volumes-from code --name django django

#dev run
sudo docker stop django-omd
sudo docker rm -v django-omd
sudo docker run -itd -v ~/Documents/git/github/vending:/volumeCode/vending -h omd --name django-omd --link mysql-django django-omd