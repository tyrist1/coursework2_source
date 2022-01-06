from flask import Flask, render_template

from utils import load_data

data, bookmarks, comments = load_data()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', posts='posts')

app.run()
