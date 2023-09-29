from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_all():
    return jsonify("hello ALL")

@app.route("/user", methods=["GET"])
def get_user():
    args = request.args
    print(args)
    user = args["user"]
    print(user)
    return jsonify(f"hello {user}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

