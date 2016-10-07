FROM wsgi

RUN useradd mod_wsgi && su mod_wsgi && cd /volumeCode/vending/django/localapp/root
#&& rm -rf /var/lib/apt/lists/* \
ENTRYPOINT ["python", "manage.py", "runmodwsgi", "--reload-on-changes","--user", "mod_wsgi"]
#USER mod_wsgi
#ENTRYPOINT ["mod_wsgi-express", "start-server", "/volumeCode/vending/django/localapp/root/root/wsgi.py"] #wsgi.py --port 8000

#COPY ./static /usr/local/apache2/htdocs/
