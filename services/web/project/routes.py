import datetime

import jwt
from . import app
from datetime import datetime as dt
from flask import jsonify, request

from .config import Config
from .models import User


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route("/register", methods=["GET", "POST"])
def register_page():
    data = request.get_json()

    new_user = User.get_by_email(data["email"])

    if new_user is not None:
        return jsonify({"message": "The email {data['email']} is being used. Try another option"})
    else:
        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])
        new_user.save()

    return jsonify({"message": "User created successfully"}), 200


@app.route("/login", methods=["GET", "POST"])
def login_page():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "could not verify"}), 401

    user = User.query.filter_by(username=auth.username).first()
    if user.check_password(auth.password):
        token = jwt.encode(
            {'id': user.id, 'exp': dt.utcnow() + datetime.timedelta(minutes=60)},
            Config.SECRET_KEY, algorithm='HS256'
        )
        return token
    else:
        return jsonify({"message": "This's not working at all"}), 500
