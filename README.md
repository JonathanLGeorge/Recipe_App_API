# Recipe_App_API

app api source code

# how to run our docker compose file

docker-compose run [servicesName] comandOnOurLinuxConainer "???"

# example

docker-compose run app sh -c "django-admin.py startproject app ."

using flake8
and https://travis-ci.org/github/JonathanLGeorge/Recipe_App_API
we git push origin to reload i think...

# tests

docker-compose run app sh -c "python manage.py test"

# docker build

docker-compose build

# adding core folder in app

docker-compose run app sh -c "python manage.py startapp core"

# docker-compose run app sh -c "python manage.py makemigrations core"

docker-compose run app sh -c "python manage.py test && flake8"
