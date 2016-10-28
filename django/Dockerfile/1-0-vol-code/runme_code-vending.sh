#!/usr/bin/env bash
sudo docker build -t code-vending:latest .
sudo docker rm code-vending && sudo docker create -v /volumeCode --name code-vending code-vending
 #/bin/true