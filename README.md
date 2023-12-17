## Clone this repo

    git clone https://github.com/u1-btj/simple-api.git

## Check requirement
### Make sure python version same as .python-version file

    python -V
    
### If not same, install that version and set on local :

    pyenv install 3.10.5
    pyenv local 3.10.5
    
If pyenv not installed, follow this link for installation : [pyenv installation](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

## Setup virtual environment
### Create virtual environment

    virtualenv venv

If virtualenv not installed, follow this link for installation : [venv installation](https://virtualenv.pypa.io/en/latest/installation.html)

### Activate virtualenv

    source venv/Scripts/activate

### Install required module on requirements.txt

    pip install requirements.txt

## Create and setup database
Execute sql script on **simple_api.sql**

## Configure database connection

On **main.py**, change following configuration into your local configuration :

    conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres',
    database='simple_api'
    )

## Run flask app in local

    python main.py
