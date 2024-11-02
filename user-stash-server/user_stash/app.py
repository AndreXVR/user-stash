from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
users_list = []


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users", methods=["POST"])
def users():
    if request.method == "POST":
        user = request.json["user"]
        response = {"user": {
            "username": request.json["user"]["username"],
            "email": request.json["user"]["email"],
            "token": "abuble"
        }}
        users_list.append(user)  # Saving users on memory, for testing without DB
    return response


@app.route("/users/login", methods=["POST"])
def login():
    if request.method == "POST":
        user = request.json["user"]
        response = {"user": {
            "username": user["username"],
            "email": user["email"],
            "token": "abuble"
        }}
    return response


if __name__ == '__main__':
    app.run(port=5000)
