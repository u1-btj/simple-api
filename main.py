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

# @app.route('/test')
# def test():
#    response = requests.request("GET", f'{base_url}{user_endpoint}/2')
#    return response.json()

if __name__ == '__main__':
   app.run()