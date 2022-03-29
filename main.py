# web scraping with beatiful soup
# The first step is parsing the html file of that particular website
# beatiful soup is a python library for pulling data out of html and xml files

from turtle import heading
from bs4 import BeautifulSoup
# import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser") #this line of code completes our parsing
print(soup.title) #<title>Angela's Personal Site</title>
print(soup.title.name) #title
print(soup.title.string) #Angela's Personal Site
print(soup) #prints the whole html site
print(soup.prettify) # nicely indents the html code

# we have only been getting the first elements, what if we want to find all the p tags, a tags etc
print(soup.find_all(name='a')) # a list of all a tags

all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.getText())
    # getting the href attribute
    print(tag.get("href"))

# getting elements using attributes
heading = soup.find(name="h1", id="name")
print(heading)
print(heading.string)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# drilling down to a particular element through other elements
company_url = soup.select_one(selector="p a")#looking for an a tag sitting iniside a p tag
print(company_url)

name= soup.select_one(selector="#name")
print(name)