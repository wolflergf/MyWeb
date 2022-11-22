from flask import Flask, render_template, url_for
import requests

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "751aa5c95c6d4ffab434a38f93f35163"
KEY_WORD = "Python, -swallows, -swallowed"


news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": KEY_WORD,
    }

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]
three_articles = articles[:4]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_articles=three_articles)


if __name__ == "__main__":
    app.run(debug=True)
