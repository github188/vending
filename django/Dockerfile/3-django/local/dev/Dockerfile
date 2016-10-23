FROM wsgi-omd-dev

# init can only work when code mapped from host is ready. so it's in CMD
COPY init.sh /
RUN useradd mod_wsgi && su mod_wsgi && chmod +x /init.sh
#&& rm -rf /var/lib/apt/lists/* \

# CMD ["/bin/bash", "/init.sh"]
# there was problem use cmd here,for the script will keep on running if container not override command part
#ENTRYPOINT ["python", "manage.py", "runmodwsgi", "--reload-on-changes", "--user", "mod_wsgi"]


#USER mod_wsgi
#ENTRYPOINT ["mod_wsgi-express", "start-server", "/volumeCode/vending/django/localapp/root/root/wsgi.py"] #wsgi.py --port 8000

#COPY ./static /usr/local/apache2/htdocs/
