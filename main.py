from flask import Flask, render_template, request, jsonify
import psycopg2
import requests
from datetime import datetime

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
@app.route('/users/<string:uid>', methods=['PUT'])
def update(uid):
    data = request.get_json() # ambil data dari body yang diberikan
    cur.execute("SELECT * FROM users WHERE user_id = " + uid)
    existing_user = cur.fetchone()

    # jika existing_user ada, maka update value sesuai user_id
    if existing_user:
        # request PUT data harus utuh, jika tidak, maka tampilkan attributes yang tidak ada
        fields = ['email', 'firstname', 'lastname', 'avatar', 'token_user']
        missing = [x for x in fields if x not in data]
        if missing:
            return jsonify({'error': f'Missing attributes: {", ".join(missing)}'}), 400
        # lakukan update sesuai dengan field body request yang diisi
        cur.execute("UPDATE users SET email = %s, firstname = %s, lastname = %s, avatar = %s, token_user = %s WHERE user_id = %s",
                    (data.get('email'), data.get('firstname'), data.get('lastname'), data.get('avatar'), data.get('token_user'), 
                    uid))
    # jika tidak ada, maka tampilkan error
    else:
        return jsonify({"error":"user does not exist"}), 404

    waktu = str(datetime.now()) # simpan timestamp update
    # mengambil nilai yang sudah di update sebelumnya
    cur.execute("SELECT * FROM users WHERE user_id = " + uid)
    updated_user = cur.fetchone()
    # pasangkan nilai dengan nama attribut/kolomnya
    attr = ['user_id', 'email', 'firstname', 'lastname', 'avatar', 'token_user']
    updated_dict = dict(zip(attr, updated_user)) 

    conn.commit() # commit perubahan pada database
    return jsonify({"updated":updated_dict, "updatedAt":waktu}), 200 # tampilkan data yang sudah di update dan timestamp nya

# Devina
@app.route('/resource/<string:rid>', methods=["GET"])
def get_single_resource(rid):
    response = requests.request("GET", f'{base_url}{resource_endpoint}/{rid}')
    return response.json()

# Pingky
@app.route('/users', methods=['GET'])
def list_users():
    # kueri SQL untuk mengambil seluruh data users
    user_query = 'SELECT * FROM simple_api.public.users'
    cur.execute(user_query)

    # mengambil semua baris hasil dari eksekusi kueri
    all_users = cur.fetchall()

    # mengubah hasilnya menjadi list of dictionaries
    users_list = []
    for user in all_users:
        user_dict = {
            'id': user[0],
            'email': user[1],
            'first_name': user[2],
            'last_name': user[3],
            'avatar': user[4],
        }
        users_list.append(user_dict)

    # mengonversi ke format JSON
    user_json = jsonify(users_list)
    return user_json

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
