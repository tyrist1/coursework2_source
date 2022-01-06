from flask import Flask, render_template

from utils import load_data, get_post_by_pk, get_comments_by_post_pk

posts, bookmarks, comments = load_data()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:pk>")
def page_single(pk):
    post = get_post_by_pk(pk)
    post_comments = get_comments_by_post_pk(pk)
    return render_template('post.html', post=post, comments=post_comments)



app.run()
