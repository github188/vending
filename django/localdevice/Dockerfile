FROM omd-ubuntu1604_python-wsgi

COPY requirements.txt /
RUN  pip install -r requirements.txt
#RUN chmod 666 /dev/ttyUSB*
#ENTRYPOINT ["python", "/volumeCode/pics/proj/manage.py", "runserver", "0.0.0.0:80"]
# send command to cashbox leads to error
#ENTRYPOINT ["python", "/volumeCode/localdevice/manage.py", "runmodwsgi", "--reload-on-changes", "--user", "mod_wsgi", "--port", "80"]
ENTRYPOINT ["python", "/vending/localdevice/manage.py", "runserver", "0.0.0.0:80"]

#python /volumeCode/pics/proj/manage.py runmodwsgi --reload-on-changes --user mod_wsgi --port 80
#COPY ./static /usr/local/apache2/htdocs/
