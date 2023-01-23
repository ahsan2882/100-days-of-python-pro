from bs4 import BeautifulSoup
from pathlib import Path
SITE_PATH = Path(
    Path(__file__).parent.resolve(),
    'website.html'
).resolve()


with open(SITE_PATH) as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
all_anchor_tags = soup.find_all(name='a')

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# print(heading)

# h3_heading = soup.find(name='h3', class_='heading')
# print(h3_heading)

company_url = soup.select_one(selector='p a')
print(company_url)
