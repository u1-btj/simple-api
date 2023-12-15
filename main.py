from flask import Flask, render_template, request
import requests
app = Flask(__name__)

base_url = 'https://reqres.in'
user_endpoint = '/api/users'
resource_endpoint = '/api/unknown'
register_endpoint = '/api/register'
login_endpoint = '/api/login'

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
@app.route('/resource', methods=["GET"])
def get_single_resource(uid):
    response = requests.request("GET", f'{base_url}{resource_endpoint}/{uid}')


# Pingky
@app.route('/users', methods=['GET'])
def list_users():
    response = requests.request("GET", f'{base_url}{user_endpoint}')
    return response.json()

# Ivander
@app.route('/users/<string:uid>', methods=["GET"])
def get_single_user(uid):
    response = requests.request("GET", f'{base_url}{user_endpoint}/{uid}')
    return response.json()

# Safira
@app.route('/delete', methods=['DELETE'])
def delete():
    response = requests.request('DELETE', f'{base_url}{user_endpoint}/2')
    return response.text, response.status_code

if __name__ == '__main__':
    app.run()
