from bs4 import BeautifulSoup
import requests
from pprint import pprint

# from pathlib import Path
# SITE_PATH = Path(
#     Path(__file__).parent.resolve(),
#     'website.html'
# ).resolve()


# with open(SITE_PATH) as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# all_anchor_tags = soup.find_all(name='a')

# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get('href'))

# # heading = soup.find(name='h1', id='name')
# # print(heading)

# # h3_heading = soup.find(name='h3', class_='heading')
# # print(h3_heading)

# company_url = soup.select_one(selector='p a')
# print(company_url)


response = requests.get('https://news.ycombinator.com/')
# print(response.text)


soup = BeautifulSoup(response.text, 'html.parser')

scores = soup.find_all(name='span', class_='score')
scores_ids = [score.get('id') for score in scores]

scores_dict = {score_id: int(score.getText().split(
)[0]) for score_id, score in zip(scores_ids, scores)}

# pprint(scores_dict)

max_score_id = max(scores_dict, key=scores_dict.get)
max_score = scores_dict[max_score_id]
titleId = max_score_id.replace('score_', '')

title = soup.find(id=titleId).find(name='span', class_='titleline').getText()
print(title, max_score)
