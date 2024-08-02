import requests
from bs4 import BeautifulSoup # type: ignore #ignore

url = 'https://pt.wikipedia.org/wiki/Porto_de_Santos'


response = requests.get(url)
response.raise_for_status()  


soup = BeautifulSoup(response.text, 'html.parser')


content = soup.find('div', {'class': 'mw-parser-output'})


paragraphs = content.find_all('p')
text = '\n'.join([para.get_text() for para in paragraphs])


with open('porto_de_santos.txt', 'w', encoding='utf-8') as file:
    file.write(text)
