import json

from flask import Flask, render_template, request

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
    return render_template('post.html', post=post, comments=post_comments, cnt_com=len(post_comments))



@app.route('/search/<s>')
def search_post(s):
    s = request.args.get('s')
    with open('data/data.json', 'r', encoding='UTF-8') as fp:
        posts = json.load(fp)

    search_s = []
    if s:
        for post in posts:
            if s in post["poster_name"]:
                search_s.append(post)
        return render_template("search.html", search_s=search_s, cnt=len(search_s))
    return render_template("search.html")



app.run()
