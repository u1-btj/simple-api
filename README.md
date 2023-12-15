
## Clone this repo

    git clone https://github.com/u1-btj/simple-api.git

## Check requirement
### Check if flask and requests module available on local

    pip list
    
### If not available, do :

    pip install flask && pip install requests

## Run flask app in local

    python main.py
    
## Create and setup database
run simple_api.sql

## Connect to database

Create connection to database:

    conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres',
    database='simple_api'
    )
