from flask import Flask, render_template, request
import requests
app = Flask(__name__)

base_url = 'https://reqres.in'
user_endpoint = '/api/users'
resource_endpoint = '/api/unknown'
register_endpoint = '/api/register'
login_endpoint = '/api/login'

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
@app.route('/update', methods = ['PUT'])
def update():
   payload = request.get_json()
   response = requests.request("PUT", f'{base_url}{user_endpoint}/2', data=payload)
   return response.json(), response.status_code
  
# Devina
@app.route('/resource', methods=["GET"])
def get_single_resource():
   response = requests.request("GET", f'{base_url}{resource_endpoint}/2')
   return response.json()

# Pingky
@app.route('/users', methods=['GET'])
def list_users():
   response = requests.request("GET", f'{base_url}{user_endpoint}')
   return response.json()

# Safira
@app.route('/delete', methods=['DELETE'])
def delete():
   response = requests.request('DELETE', f'{base_url}{user_endpoint}/2')
   return response.text, response.status_code

if __name__ == '__main__':
   app.run()
