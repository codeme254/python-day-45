from operator import itemgetter
from bs4 import BeautifulSoup
import requests 

# https://www.empireonline.com/movies/features/best-movies-2/
website = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(website.text, "html.parser")

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
# all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)
# listicle-item
# h3

titles = soup.select(selector="div h3")
print(titles)
