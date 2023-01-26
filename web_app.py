from flask import Flask, request
from db_connector import get_user
import os
import signal

app = Flask(__name__)

users = {}


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.route("/users/get_user_name/<user_id>", methods=['GET'])
def get_user_name(user_id):
    if request.method == 'GET':
        user_name = get_user(user_id)
        if get_user(user_id):
            return "<H1 id='user_id'>" + user_name[0][1] + "</H1>"
        else:
            return "<H1 id='error'>""no such user id: " + user_id + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)


