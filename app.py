from flask import Flask, render_template, jsonify, url_for
import json


app = Flask (__name__)


@app.route('/')
# @app.route('"C:\Users\Nyan\Desktop\visual\visual.html"')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + "-" + str(id)


if __name__ == "__main__":
    app.run(debug=True)
