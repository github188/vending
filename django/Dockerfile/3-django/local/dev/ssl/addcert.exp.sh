#!/usr/bin/expect
# https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-ubuntu-14-04

spawn openssl req -x509 -nodes -days 730 -newkey rsa:2048 -keyout ./omd-dev-local.key -out ./omd-dev-local.crt
set timeout 2
expect "Country Name (2 letter code) \[AU\]:"
send "CN\r"
#set timeout 2
expect "State or Province Name (full name) \[Some-State\]:"
send "Guangdong\r"
#set timeout 2
expect "Locality Name (eg, city) \[\]:"
send "Dongguan\r"
#set timeout 2
expect "Organization Name (eg, company) \[Internet Widgits Pty Ltd\]:"
send "Oursmedia\r"
#set timeout 2
expect "Organizational Unit Name (eg, section) \[\]:"
send "dev\r"
#set timeout 2
expect "Common Name (e.g. server FQDN or YOUR name) \[\]:"
send "oursmedia.cn\r"
#set timeout 2
expect "Email Address \[\]:"
send "jeson.peng@gmail.com\r"
#set timeout 2
interact