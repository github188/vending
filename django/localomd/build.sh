#!/usr/bin/env bash

#sudo docker stop omddata_local
#sudo docker rm omddata_local
#sudo docker rm omddata-datacontainer

#build container
sudo docker build -t omddata_local .

#create data container, just need once
#sudo docker create -v /omddata-datacontainer --name omddata-datacontainer omddata_local true

#run container
sudo docker run -itd --volumes-from omddata-datacontainer \
--network omd-dev-local --ip 172.18.0.4 --network-alias omddata_local --name omddata_local \
--restart=unless-stopped omddata_local
