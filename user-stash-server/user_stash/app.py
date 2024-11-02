from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
users_list = []


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return users_list
    if request.method == "POST":
        response = {}
        user = request.json["user"]
        if user["email"] not in [u["email"] for u in users_list]:
            response = {"user": {
                "username": request.json["user"]["username"],
                "email": request.json["user"]["email"],
                "token": "abuble"
            }}
            users_list.append(user)  # Saving users on memory
            return response
        return "Email already registered.", 401


@app.route("/users/login", methods=["POST"])
def login():
    if request.method == "POST":
        response = {}
        user = request.json["user"]
        for u in users_list:
            if user["email"] == u["email"] and user["password"] == u["password"]:
                response = {"user": {
                    "username": u["username"],
                    "email": u["email"],
                    "token": "abuble"
                }}
        if response:
            return response
        return "Invalid email or password.", 401


if __name__ == '__main__':
    app.run(port=5000)
