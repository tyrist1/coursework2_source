import json
from pprint import pprint


def load_data():
    with open('data/data.json', 'r', encoding='UTF-8') as fp:
        posts = json.load(fp)
    # \n как сделать новую строку
    with open('data/comments.json', 'r', encoding='UTF-8') as fp:
        comments = json.load(fp)
    posts = prepare_post (posts, comments)
    with open('data/bookmarks.json', 'r', encoding='UTF-8') as fp:
        bookmarks = json.load(fp)
    return posts, comments, bookmarks

def prepare_post(posts, comments):

    for i, post in enumerate(posts):
        pk = post["pk"] #  что за get?
        post_comments=[]
        for comment in comments:
            if comment.get("post_id") == pk:
                post_comments.append(comment)
        posts[i]["comments_count"] = len(post_comments)

        posts[i]["content"] = tagify_content(posts[i]["content"])
    return posts

def tagify_content(content):

    words = content.split(" ")
    for i, word in enumerate(words):
        if word.startswith("#"):
            tag=word.replace("#", "")
            link = f"<a href=' /tag/{tag}'>{word}</a>"
            words[i] = link
    return " ".join(words)

def get_post_by_pk(pk):
    with open('data/data.json', 'r', encoding='UTF-8') as fp:
        posts = json.load(fp)
    for post in posts:
        if post["pk"] == pk:
            return post

def get_comments_by_post_pk(post_pk):
    with open('data/comments.json', 'r', encoding='UTF-8') as fp:
        comments = json.load(fp)

    post_comments =[]

    for comment in comments:
        if comment["post_id"] == post_pk:
            post_comments.append(comment)
    return  post_comments

def seach_post(s):
    with open('data/data.json', 'r', encoding='UTF-8') as fp:
        posts = json.load(fp)





