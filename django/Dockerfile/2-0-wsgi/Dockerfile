FROM 2-python3

RUN pip3 install mod_wsgi-httpd && pip3 install mod_wsgi \
 && useradd mod_wsgi && su mod_wsgi
#&& rm -rf /var/lib/apt/lists/* \
USER mod_wsgi

ENTRYPOINT ["mod_wsgi-express", "start-server", "/volumeCode/vending"] #wsgi.py --port 8000

#COPY ./static /usr/local/apache2/htdocs/
