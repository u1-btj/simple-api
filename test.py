import requests
from flask import Flask, request

app = Flask(__name__)

# Mengambil data user dengan ID tertentu
@app.route('/users/<string:uid>', methods = ["GET"])
def get_single_user(uid):
    url = ("https://reqres.in/api/users/" + uid) 
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text
 
# main driver function
if __name__ == '__main__':
    app.run()

# # Ivander
# @app.route('/users/<string:uid>', methods = ["GET"])
# def get_single_user(uid):
#    # url = ("https://reqres.in/api/users/" + uid)
#    response = requests.request("GET", f'{base_url}{user_endpoint}/{uid}', headers={}, data={})
#    return response.json()