from bs4 import BeautifulSoup as bs
from pathlib import Path

SITE_PATH = Path(
    Path(__file__).parent.resolve(),
    '100-movies.html'
).resolve()

MOVIES_FILE_PATH = Path(
    Path(__file__).parent.resolve(),
    'movies.txt'
).resolve()
print(SITE_PATH)

with open(SITE_PATH, 'r') as file:
    response = file.read()
soup = bs(response, 'html.parser')

items = soup.find_all(name='div', class_='listicle-item')
movies = [item.find(name='h3').getText().strip() for item in items]
movies.reverse()

with open(MOVIES_FILE_PATH, 'w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
