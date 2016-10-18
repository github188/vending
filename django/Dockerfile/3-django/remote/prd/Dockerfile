FROM omd-local

CMD ["python", "/volumeCode/vending/django/localomd/manage.py", "runmodwsgi", "--user", "mod_wsgi", "--host", "0.0.0.0", "--port", "80"]
#ENTRYPOINT ["python"]


#USER mod_wsgi
#ENTRYPOINT ["mod_wsgi-express", "start-server", "/volumeCode/vending/django/localapp/root/root/wsgi.py"] #wsgi.py --port 8000

#COPY ./static /usr/local/apache2/htdocs/
