from flask import Flask, jsonify
import platform
import sys
import subprocess
import requests

app = Flask(__name__)
response = requests.get(url="http://127.0.0.1:5000/task")
def datos():
    data = response.json()
    print("Nombre " + data['hostname'])
    print("IP " + data['local_ip'])
datos()

if __name__ == '__main__':
    app.run(debug=True, port= 3000)