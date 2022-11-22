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
three_articles = articles[:3]
print(three_articles)
