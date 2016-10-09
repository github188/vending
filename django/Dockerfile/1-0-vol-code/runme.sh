#!/usr/bin/env bash
sudo docker build -t code:latest .
sudo docker rm code && sudo docker create -v /volumeCode --name code code
 #/bin/true