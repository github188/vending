FROM omd-ubuntu1604_python-wsgi

COPY requirements.txt /
RUN  pip install -r requirements.txt \
&& useradd mod_wsgi && su mod_wsgi && rm -rf /var/lib/apt/lists/*

#dont copy to avoid building container for code changes
#COPY . /vending/localomd

#VOLUME ["/vending/localomd/db.sqlite3"]
ENTRYPOINT ["python", "/vending/localomd/manage.py", "runserver", "0.0.0.0:80"]
#ENTRYPOINT ["python", "/vending/localomd/manage.py", "runmodwsgi", "--reload-on-changes", "--user", "mod_wsgi", "--port", "80"]
#python /volumeCode/pics/proj/manage.py runmodwsgi --reload-on-changes --user mod_wsgi --port 80
#COPY ./static /usr/local/apache2/htdocs/
