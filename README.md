# ticket backend


## directory

```
├── app.py                  # initial flask app 
├── apps/ # applications 
│ ├── {app_name}/           
    │ ├── __init__.py # initial app
    │ ├── models.py # app model
    │ ├── views.py # app controller
├── common/ # shared in general 
├── configs.py # configures(modify for different environment)
├── manage.py # flask manager
```

## deployment



### create and setup conda env

```sh

pip install tqdm flask flask-sqlalchemy flask-cors flask-migrate   requests  flask-jwt-extended  psycopg2-binary pymysql
```




### create database and setup user



### init db

```sh
flask db init
flask db migrate
flask db upgrade
```

### start app

#### start with gunicorn(production)



```sh
flask run --reload
```
