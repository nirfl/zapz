from flask import Flask, jsonify, request
import getpass
import datetime




app = Flask(__name__)

connected_users ={}

@app.route('/')
def hello_world():
    result = "logged users:\n"
    for user in connected_users:
        formatted_datetime = connected_users[user].strftime("%Y-%m-%d %H:%M:%S")
        s = f"{user} logged in time:{formatted_datetime}"
        result+= s+"\n"
    return jsonify(result)
@app.route("/user", methods=["GET"])
def get_user():
    current_datetime = datetime.datetime.now()
    args = request.args
    print(args)
    user = args["user"]
    connected_users[user] = current_datetime
    print(user)
    return jsonify(f"hello {user}. You are connected to {getpass.getuser()}")

if __name__ == '__main__':
    app.run(host='0.0.0.0')