FROM omd-apache2-prd
# digitaiocean how to serve django-application with apache and modwsgi on ubuntu 14 04
# https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-ubuntu-14-04
RUN apt-get install -y nano\
#&& python3 python3-dev
python3-pip libapache2-mod-wsgi-py3 libmysqlclient-dev \
&& ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip
&& pip install django mysqlclient
&& cd /etc/apache2/sites-available
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ Alias \/static\ \/opt\/myproject\/static" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ <Directory\ \/opt\/myproject\/static>" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ \ \ \ \ Require\ all\ granted" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ <\/Directory>" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ <Directory\ \/opt\/myproject\/myproject>" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ \ \ \ \ <Files\ wsgi.py>" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Require\ all\ granted" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ \ \ \ \ <\/Files>" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ <\/Directory>" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ WSGIDaemonProcess\ myproject\ python-path=\/opt\/myproject" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ WSGIProcessGroup\ myproject" 000-default.conf \
&& sed -i "/<\/VirtualHost>/i\ \ \ \ \ \ \ \ WSGIScriptAlias\ \/\ \/opt\/myproject\/myproject\/wsgi.py" 000-default.conf \

&& sed -i 's/\/etc\/ssl\/certs\/ssl-cert-snakeoil.pem/\/volumeCode\/vending\/django\/Dockerfile\/3-django\/local\/dev\/ssl\/omd-dev-local.crt/1' default-ssl.conf \
&& sed -i 's/\/etc\/ssl\/private\/ssl-cert-snakeoil.key/\/volumeCode\/vending\/django\/Dockerfile\/3-django\/local\/dev\/ssl\/omd-dev-local.key/1' default-ssl.conf \
&& a2ensite default-ssl.conf

#&& chmod 664 /opt/myproject/db.sqlite3
&& chown :www-data /opt/myproject
#&& chown :www-data /opt/myproject/db.sqlite3
CMD ["apache2", "start"]


#&& pip3 install --upgrade pip && ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3 /usr/bin/pip \
#&& pip install mod_wsgi django mysqlclient