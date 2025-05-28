import requests
import os

API_KEY = os.getenv("NEWS_API_KEY")
COUNTRY = os.getenv("NEWS_COUNTRY", "us")
URL = f"https://newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey={API_KEY}"

response = requests.get(URL)
if response.status_code == 200:
    articles = response.json().get("articles", [])
    with open("output.txt", "w") as f:
        for article in articles[:5]:
            f.write(f"{article['title']}\n")
    print("News headlines saved to output.txt")
else:
    print(f"Failed to fetch news: {response.status_code}, {response.text}")

