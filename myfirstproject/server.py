from flask import Flask, jsonify, request
import getpass

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify('Hello, Michal1')

@app.route("/user", methods=["GET"])
def get_user():
    args = request.args
    print(args)
    user = args["user"]
    print(user)
    return jsonify(f"hello {user}. You are connected to {getpass.getuser()}")

if __name__ == '__main__':
    app.run(host='0.0.0.0')