import json
from pprint import pprint


def load_data():
    with open('data/data.json', 'r', encoding='UTF-8') as fp:
        posts = json.load(fp)
    # \n как сделать новую строку
    with open('data/comments.json', 'r', encoding='UTF-8') as fp:
        comments = json.load(fp)
    posts = comments_go_to_post(posts, comments)
    with open('data/bookmarks.json', 'r', encoding='UTF-8') as fp:
        bookmarks = json.load(fp)
    return posts, comments, bookmarks

def comments_go_to_post(posts,comments):

    for i, post in enumerate (posts):
        pk = post.get('pk') #  что за get?
        post_comments=[]
        for comment in comments:
            if comment.get("post_id") == pk:
                post_comments.append(comment)
        posts[i]['comments'] = post_comments
    return posts



