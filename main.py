import flask
from flask import request
import csv
import random

app = flask.Flask(__name__)

with open('tweets.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

count = len(rows)

@app.route('/')
@app.route('/tweets/tech_satire')
def get_tech_satire_quote():
    n = random.randrange(count)
    tweet = rows[n]
    screen_name, pretty_name, tweet_id, created_at, text = tweet



    if 'Content-Type' not in request.headers or request.headers['Content-Type'] == 'text/plain':
        return text + " ~ " + pretty_name

    elif request.headers['Content-Type'] == 'application/json':
        return {
            "tweet": text,
            "author": pretty_name,
            "handle": screen_name,
            "tweet_id": tweet_id,
            "date": created_at,
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
