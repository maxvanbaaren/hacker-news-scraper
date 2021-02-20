from bs4 import BeautifulSoup as bs
import requests

url = 'https://news.ycombinator.com/'
r = requests.get(url).text
soup = bs(r, "html.parser")

for article in soup.find_all(class_='storylink'):
    print(article.text)
    print(article['href'])
    print()

