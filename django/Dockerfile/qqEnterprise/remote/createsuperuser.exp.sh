#!/usr/bin/expect
# https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-ubuntu-14-04

spawn python ../../qqEnterprise/manage.py createsuperuser --username pjsong --email admin@oursmedia.cn
set timeout 2
expect "Password:"
send "pjsong3101\r"
#set timeout 2
expect "Password (again):"
send "pjsong3101\r"
#set timeout 2
interact