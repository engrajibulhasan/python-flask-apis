
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, make_response, request

from utils.shared_utils import generate_hash

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! UPDATED'


@app.route('/users/')
def users():
    data=[
            {
            "username":"rajibul",
            "mobile":"01727843493"
            },
            {
            "username":"naim",
            "mobile":"01647848493"
            }
        ]
    res=make_response(jsonify(data))
    return res

@app.post('/registration')
def create_user():
    username=request.form.get("username",None)
    full_name=request.form.get("full_name",None)
    password=request.form.get("password",None)
    re_password=request.form.get("re_password",None)
    combine_data={
        "username":username,
        "full_name":full_name,
        "password":generate_hash(password),
        "re_password":generate_hash(re_password),

    }
    res=make_response(jsonify(combine_data))
    return res