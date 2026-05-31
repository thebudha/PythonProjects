import requests
from bs4 import BeautifulSoup

response = requests.get('https://stackoverflow.com/questions')
soup = BeautifulSoup(response.text, 'html.parser')

questions = soup.select(".s-post-summary--content")
#print(questions[0].select_one(".s-link").getText())

for question in questions:
    print(question.select_one(".s-link").getText())

    