from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/'
result = requests.get(website)

soup = BeautifulSoup(result.text, 'lxml')
latest_added_transcripts = soup.find('article').get_text().split('\n')
latest_added_transcripts = [
    title for title in latest_added_transcripts if title]

content = '\n'.join(map(str, latest_added_transcripts[1:]))

with open(f'latest-movies-list.txt', 'w') as file:
    file.write(content)
