#!/usr/bin/env bash

#sudo docker stop omddata_local
#sudo docker rm omddata_local
#sudo docker rm omddata-datacontainer

#build container
sudo docker build -t omddata_local .

#create data container, just need once
#sudo docker create -v /omddata-datacontainer --name omddata-datacontainer omddata_local true
#changed to data-volume, because it's more convenient for code changes.
# before thought the container images can be save together with volume,
# infacto not, and this target image was not to be resued

#run container
sudo docker run -d -v ~/vending/localomd:/vending/localomd --network=omd-network \
 --ip=172.18.0.2 -h omddata
 --name omddata --restart=unless-stopped omddata_local

