FROM 0-ubuntu-updated

RUN apt-get install -y python3 python3-pip libmysqlclient-dev && pip3 install --upgrade pip && ln -s /usr/bin/python3 /usr/bin/python  \
&& pip3 install mod_wsgi-httpd && pip3 install mod_wsgi && pip3 install django && pip3 install mysqlclient
