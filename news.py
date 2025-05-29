import requests
import os

def get_news(api_key):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        "apiKey": api_key,
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    return [article["title"] for article in articles if "title" in article]

def save_news_to_file(news_list, filename="output.txt"):
    with open(filename, "w") as f:
        for title in news_list:
            f.write(f"{title}\n")

if __name__ == "__main__":
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("NEWS_API_KEY environment variable not set")
    news = get_news(api_key)
    save_news_to_file(news)
    print("News headlines saved to output.txt")
