FROM wsgi-omd

RUN useradd mod_wsgi && su mod_wsgi \
&& echo "cd /volumeCode/vending/django/localapp/root; python manage.py collectstatic --noinput; python manage.py runmodwsgi --reload-on-changes --user mod_wsgi;" > /init.sh \
&& chmod +x /init.sh
#&& rm -rf /var/lib/apt/lists/* \
CMD ["/bin/bash", "/init.sh"]
#ENTRYPOINT ["python", "manage.py", "runmodwsgi", "--reload-on-changes", "--user", "mod_wsgi"]


#USER mod_wsgi
#ENTRYPOINT ["mod_wsgi-express", "start-server", "/volumeCode/vending/django/localapp/root/root/wsgi.py"] #wsgi.py --port 8000

#COPY ./static /usr/local/apache2/htdocs/
