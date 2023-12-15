from flask import Flask, render_template, request
import psycopg2
# import requests
import json

app = Flask(__name__)

base_url = 'https://reqres.in'
user_endpoint = '/api/users'
resource_endpoint = '/api/unknown'
register_endpoint = '/api/register'
login_endpoint = '/api/login'

# Konfigurasi koneksi PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='postgres',
    database='simple_api'
)

# Membuat kursor
cur = conn.cursor()

@app.route('/')
def home():
    return render_template('index.html', local_url=request.base_url)

# Ivander
@app.route('/users/<string:uid>', methods=["GET"])
def get_single_user(uid):
    #query ambil user
    user_query = 'select * from simple_api.public.users where user_id = ' + uid
    cur.execute(user_query)
    user = cur.fetchone()
    # kalau user tidak ada
    if(user==None):
        return {'error': 'not found'}, 404
    else:
        user_json = {
            'id': user[0],
            'email': user[1],
            'first_name': user[2],
            'last_name': user[3],
            'avatar': user[4]
        }
        user_json = json.dumps(user_json)
        return user_json

if __name__ == '__main__':
    app.run(debug=True)
