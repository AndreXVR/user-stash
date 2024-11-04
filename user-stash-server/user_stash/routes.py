from os import environ

import jwt
from flask import Blueprint, jsonify, request

from user_stash.models import User
routes_bp = Blueprint("auth", __name__)


JWT_SECRET = environ.get("FLASK_SECRET_KEY")


def auth_token(request):
    auth = request.headers.get("Authorization")
    if not auth:
        return None
    token = auth.split(" ")[-1]
    try:
        jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return token
    except:  # noqa: E722
        return None


@routes_bp.post("/register")
def register():
    data = request.get_json().get("user")
    user = User.read_by_email(email=data.get("email"))

    if user:
        return "User already exists", 401

    new_user = User(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        admin=False,
        active=True
    )
    new_user.hash_password(password=data.get("password"))
    token = jwt.encode({"email": new_user.email}, JWT_SECRET)
    new_user.create()
    return jsonify({
        "user": {"first_name": new_user.first_name,
                 "last_name": new_user.last_name,
                 "email": new_user.email,
                 "token": token}
    })


@routes_bp.post("/login")
def login():
    data = request.get_json().get("user")

    user = User.read_by_email(email=data.get("email"))

    if not user or not user.check_password(data.get("password")):
        return "Invalid email or password", 401

    token = jwt.encode({"email": user.email}, JWT_SECRET)
    return jsonify({
        "user": {"first_name": user.first_name,
                 "last_name": user.last_name,
                 "email": user.email,
                 "token": token}
    })


@routes_bp.get("/user")
def get_user():
    token = auth_token(request)
    if not token:
        return jsonify({"error": "Authorization failed"}), 403
    payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    user = User.read_by_email(email=payload.get("email"))
    return jsonify({
        "user": {"first_name": user.first_name,
                 "last_name": user.last_name,
                 "email": user.email,
                 "token": token}
    })


@routes_bp.post("/user/update")
def update_user(token=None):
    token = auth_token(request)
    if not token:
        return jsonify({"error": "Authorization failed"}), 403
    payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    user = User.read_by_email(email=payload.get("email"))
    data = request.get_json().get("user")
    if User.read_by_email(email=data.get("email")) and data.get("email") != user.email:
        return "Email already in use", 400

    if not user.check_password(data.get("old_password")):
        return "Invalid password", 400

    user.update(data.get("first_name"),
                data.get("last_name"),
                data.get("email"),
                data.get("new_password")
                )
    token = jwt.encode({"email": user.email}, JWT_SECRET)
    return jsonify({
        "user": {"first_name": user.first_name,
                 "last_name": user.last_name,
                 "email": user.email,
                 "token": token}
    })
