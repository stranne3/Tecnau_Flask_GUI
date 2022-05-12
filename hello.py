from flask import Flask
from flask import render_template
from flask import jsonify
from time import time
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



@app.route("/count", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('start'):
            for i in range(5,0,-1):
                print(i)
                time.sleep(1)
                return render_template("index.html", i)
