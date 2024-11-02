from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
users_list = []


@app.route("/api")
def hello_world():
    return "<p>User Stash :)</p>"


@app.route("/api/user", methods=["GET"])
def user():
    if request.method == "GET":
        auth = request.headers.get("Authorization")
        token = auth[6:] if auth else ""
        if token:
            for user in users_list:
                if token == user.get("token"):
                    return {"user": {
                        "username": user.get("username"),
                        "email": user.get("email"),
                        "token": user.get("token")
                    }}
        return "Unauthorized, please log in", 401


@app.route("/api/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return users_list
    if request.method == "POST":
        response = {}
        user = request.json.get("user")
        if user.get("email") not in [u.get("email") for u in users_list]:
            user.update({"token": "t"+user.get("email")})
            response = {"user": {
                "username": user.get("username"),
                "email": user.get("email"),
                "token": user.get("token")
            }}
            users_list.append(user)  # Saving users on memory
            return response
        return "Email already registered.", 401


@app.route("/api/users/login", methods=["POST"])
def login():
    if request.method == "POST":
        response = {}
        user = request.json.get("user")
        for u in users_list:
            if user["email"] == u["email"] and user["password"] == u["password"]:
                user.update({"token": "t"+user.get("email")})
                response = {"user": {
                    "username": user.get("username"),
                    "email": user.get("email"),
                    "token": user.get("token")
                }}
                break
        if response:
            return response
        return "Invalid email or password.", 401


if __name__ == '__main__':
    app.run(port=5000)
