from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    # return "<h1>Hello, World!</h1>"
    return "Hello, World!"


@app.route("/hello1")
def hello_world1():
    # return "<h1>Hello, World!</h1>"
    return "Hello, World! 1"


@app.route("/hello2")
def hello_world2():
    # return "<h1>Hello, World!</h1>"
    return "Hello, World! 2"


@app.route("/test_fun")
def test():
    a = 5 + 6
    return f"this is my first fun in flask, a: {a}"

# @app.route("input_url")  # ValueError: urls must start with a leading slash
@app.route("/input_url")  # http://127.0.0.1:5000/input_url?x=data%20science
def request_input():
    data = request.args.get("x")
    return f"this is my input from url {data}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

# 5000 is the default port number in Flask
