from flask import Flask
import requests
app = Flask(__name__)

base_url = 'https://reqres.in'
user_endpoint = '/api/users'
resource_endpoint = '/api/unknown'


@app.route('/devina')
def test():
   response = requests.request("GET", f'{base_url}{user_endpoint}/2')
   return response.json()

if __name__ == '__main__':
   app.run()