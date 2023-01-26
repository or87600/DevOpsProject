from flask import Flask, request, make_response, jsonify
from db_connector import get_user
from stop_flask_server import StopFlaskServer


app = Flask(__name__)

users = {}


@app.route("/users/get_user_name/<user_id>", methods=['GET'])
def get_user_name(user_id):
    if request.method == 'GET':
        user_name = get_user(user_id)
        if get_user(user_id):
            return "<H1 id='user_id'>" + user_name[0][1] + "</H1>"
        else:
            return "<H1 id='error'>""no such user id: " + user_id + "</H1>"


@app.route('/stop_server', methods=['GET'])
def stop_web_server():
    if request.method == 'GET':
        obj_stop_r_server = StopFlaskServer
        if obj_stop_r_server.stop_flask_server() is True:
            response = make_response(
                jsonify(
                    {
                        "status": "web server successfully stopped",
                        "is died": True
                    }
                )
            )

            response.headers['Content-Type'] = 'application/json'
            return response, 200


app.run(host='127.0.0.1', debug=True, port=5001)


