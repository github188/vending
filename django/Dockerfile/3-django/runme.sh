#!/usr/bin/env bash
sudo docker build -t 3-django:latest .

#prod run
sudo docker run -d --volumes-from vol-code --name wsgi 3-django

#dev run
sudo docker run -it -v ~/Documents/git/github/vending:/volumeCode/vending --name local-django 3-django bash