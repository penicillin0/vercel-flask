from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# json response
@app.route("/json")
def about():
    return {"name": "John Doe", "age": 30, "city": "New York"}
