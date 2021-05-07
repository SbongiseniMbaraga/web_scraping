from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
article_text = article_tag.text
article_link = article_tag.get("href")
article_upvote = soup.find(name="span", class_="score")
article_upvote = article_upvote.getText()






