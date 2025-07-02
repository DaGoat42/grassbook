from flask import Flask, render_template
from time import time
import humanize

app = Flask(__name__)

exampleposts = [
    {
        "title": "Look up, theres an airplane!",
        "body": "I lost the game",
        "user": "jeffrey",
        "time": 1750275751
    }
]

def process_times(posts):
    for post in posts:
        time_diff = time() - post["time"]
        time_readable = humanize.naturaltime(time_diff)
        post["time_readable"] = time_readable

    return posts

@app.route("/")
def homepage():
    posts_processed = process_times(exampleposts)
    return render_template("homepage.html", posts = posts_processed)

if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)
