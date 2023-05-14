import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com/'
result = requests.get(root)

soup = BeautifulSoup(result.text, 'lxml')
article = soup.find('article')
box = article.find('ul', class_="scripts-list")
latest_movies_transcripts = box.find_all('a', href=True)

links = []
for movie in latest_movies_transcripts:
    links.append(movie['href'])

for link in links:
    try:
        result = requests.get(f'{root}/{link}')
        soup = BeautifulSoup(result.text, 'lxml')
        title = soup.find('h1').get_text()
        box = soup.find('div', class_="full-script")
        content = box.get_text(strip=True, separator=' ')
        print(content)
        with open(f'{title}.txt', 'w') as file:
            file.write(content)
    except:
        print('Issue')
