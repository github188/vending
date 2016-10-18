#!/usr/bin/env bash
sudo docker build -t omd-dev-remote .
# docker network create --subnet 172.16.0.0/12 omd-remote-dev

#dev run
sudo docker stop local-omd
sudo docker rm -v local-omd

sudo docker run -itd -v ~/Documents/git/github/vending:/volumeCode/vending \
--network omd-dev-remote --ip 172.18.0.4 --name omd-remote omd-remote bash