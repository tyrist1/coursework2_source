from flask import Flask, request, render_template, abort, url_for
import os
from utils import load_data, comments_go_to_post

data, bookmarks, comments = load_data()
# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', posts='posts')
 # 'posts'  = почему у тебя работает без кавычек
app.run(debug=True)