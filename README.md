# Install postgresql and other things

Create Virtual Environment: python3 -m venv env
Activate Env: source/env/activate
Install Django and psycopg2-binary:
pip3 install django
pip3 install psycopg2-binary
Create Python Project and it’s app:
django-admin startproject core .
django-admin startappp pdjango


#####################################################################################################################################################
# Create Databse , Username, Password

Ctrl + Alt + T, Open Terminal and Type: sudo -u postgres psql
CREATE DATABASE mydb;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypass';
ALTER ROLE myuser SET client_encoding TO 'utf8';
ALTER ROLE myuser SET default_transaction_isolation TO 'read
committed';
ALTER ROLE myuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

##################################################################

Finally,  \q to quit the  psql.

Now write the below script into the settings.py:

# Settings.py

###############################################################


DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'test',
       'USER': 'test',
       'PASSWORD': '12345',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}
###############################################################

# END
