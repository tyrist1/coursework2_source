import json

from flask import Flask, render_template, request

from utils import load_data, get_post_by_pk, get_comments_by_post_pk,search_posts_by_text, get_posts_by_users

posts, bookmarks, comments = load_data()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:pk>")
def page_single(pk):
    post = get_post_by_pk(pk)
    post_comments = get_comments_by_post_pk(pk)
    return render_template('post.html', post=post, comments=post_comments, cnt_com=len(post_comments))

@app.route('/search/')
def search_post():
    s = request.args.get('s')
    search_s = search_posts_by_text(s)
    return render_template("search.html", posts=search_s, cnt=len(search_s))
    # return render_template("search.html")


@app.route("/users/<username>")
def page_user(username):

    posts = get_posts_by_users(username)
    return render_template('user-feed.html', posts=posts )


if __name__ == "__main__":
    app.run()
