#!/usr/bin/env bash

#sudo docker create -v /omddevice-datacontainer --name omddevice-datacontainer localdevice true

#dev run
sudo docker stop omddevice
sudo docker rm -v omddevice

#sudo docker run -itd -v ~/Documents/git/github/vending/django/localdevice:/volumeCode/localdevice \
#-v ~/Documents/git/bitbucket/itl-validator/libBasicValidator:/home/pjsong/Documents/git/bitbucket/itl-validator/libBasicValidator \
#--network omd-dev-local --ip 172.18.0.6 --network-alias localdevice --name localdevice \
#--restart=unless-stopped --privileged localdevice

sudo docker run -d -v ~/vending/localdevice:/vending/localdevice \
-v ~/vending/lib/libBasicValidator:/vending/lib/libBasicValidator \
--name omddevice \
--restart=unless-stopped --privileged omddevice

#python ../../../../proj/manage.py runserver 0.0.0.0:80 > /dev/null 2>&1 &
#python manage.py runmodwsgi --reload-on-changes --user mod_wsgi --host 0.0.0.0 --port 80  > /dev/null 2>&1 &;