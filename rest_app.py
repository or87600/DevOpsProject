from flask import Flask, request
from db_connector import add_user, get_user, delete_user, update_user
import os
import signal

app = Flask(__name__)

users = {}


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        getuser = get_user(user_id)
        return {'user_id': getuser[0][0], 'user_name': getuser[0][1]}, 200

    elif request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        add_user(user_id, user_name)
        return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200

    elif request.method == 'DELETE':
        userid = delete_user(user_id)
        return {"status": "deleted", "user_deleted": userid}, 200

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        update_user(user_id, user_name)
        return {"status": "updated", "user_updated": user_name}, 200


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
