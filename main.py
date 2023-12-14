from flask import Flask
import requests
app = Flask(__name__)

base_url = 'https://reqres.in'
user_endpoint = '/api/users'
resource_endpoint = '/api/unknown'

'''
Ivan -> Single User
Devina -> Create User
Pingky -> List User
Safira -> Delete User
Faiz -> Update User Put
Yuma -> Get List Resource
'''

@app.route('/test')
def test():
   # Contoh get user id 2
   response = requests.request("GET", f'{base_url}{user_endpoint}/2')
   return response.json()

@app.route('/test-yuma')
def test():
   response = requests.request("GET", f'{base_url}{user_endpoint}/2')
   return response.json()

if __name__ == '__main__':
   app.run()