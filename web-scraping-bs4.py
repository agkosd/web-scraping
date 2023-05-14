import requests
from bs4 import BeautifulSoup

result = requests.get(
    'https://subslikescript.com/movie/Blind_Detective-2332707')

soup = BeautifulSoup(result.text, 'lxml')
box = soup.find('article', class_="main-article")

title = box.find('h1').get_text()
full_script = box.find(
    'div', class_="full-script").get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w') as file:
    file.write(full_script)
