#!/usr/bin/python3

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    # sr = "/wholesomemes"
    # url = "https://meme-api.herokuapp.com/gimme" + sr
    api_array = ["https://meme-api.com/gimme"]
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html",
                           meme_pic=meme_pic,
                           subreddit=subreddit)

app.run(host="0.0.0.0", port=80)
