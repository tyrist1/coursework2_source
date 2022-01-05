from flask import Flask, request, render_template, abort, url_for
import os
from utils import ...

# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)