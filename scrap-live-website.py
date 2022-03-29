from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find(name="a", class_="titlelink")
print(article_tag.getText())

article_links = soup.find_all(name="a", class_="titlelink")
for link in article_links:
    print(link.getText())
    print(link.get("href"))
    print("--------------")

article_upvotes = soup.find_all(name="span", class_="score")

for vote in article_upvotes:
    print(vote.getText())
    print("--------------")