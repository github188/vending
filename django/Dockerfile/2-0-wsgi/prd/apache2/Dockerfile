FROM 0-ubuntu-updated

RUN rm -rf /var/lib/apt/lists/* \
#&& apt-get update && apt-get install -y apache2 apache2-dev libapache2-mod-wsgi && a2enmod wsgi \
&& apt-get update && apt-get install -y apache2 && a2enmod ssl
#&& python3-pip libapache2-mod-wsgi-py3 && a2enmod wsgi \
#&& ln -s /usr/bin/pip3 /usr/bin/pip \
#&& rm -rf /var/lib/apt/lists/* && apt-get update