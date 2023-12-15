from flask import Flask, render_template, request, jsonify
import psycopg2
import requests

app = Flask(__name__)
app.json.sort_keys = False

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

# Yuma
@app.route('/register', methods=['POST'])
def register():
    payload = request.get_json()
    response = requests.request("POST", f'{base_url}{register_endpoint}', data=payload)
    return response.json(), response.status_code

# Faiz
@app.route('/update/<string:uid>', methods=['PUT'])
def update(uid):
    payload = request.get_json()
    response = requests.request("PUT", f'{base_url}{user_endpoint}/{uid}', data=payload)
    return response.json(), response.status_code

# Devina
@app.route('/resource/<string:rid>', methods=["GET"])
def get_single_resource(rid):
    response = requests.request("GET", f'{base_url}{resource_endpoint}/{rid}')
    return response.json()

# Pingky
@app.route('/users', methods=['GET'])
def list_users():
    response = requests.request("GET", f'{base_url}{user_endpoint}')
    return response.json()

# Ivander
@app.route('/users/<string:uid>', methods=["GET"])
def get_single_user(uid):
    #query ambil data user
    user_query = 'select * from simple_api.public.users where user_id = ' + uid
    cur.execute(user_query)
    user = cur.fetchone()
    # kalau user tidak ada
    if(user==None):
        return {'error': 'user not found'}, 404
    else:
        user_json = {
            'id': user[0],
            'email': user[1],
            'first_name': user[2],
            'last_name': user[3],
            'avatar': user[4]
        }
        user_json = jsonify(user_json)
        return user_json

# Safira
@app.route('/delete', methods=['DELETE'])
def delete():
    response = requests.request('DELETE', f'{base_url}{user_endpoint}/2')
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(debug=True)
