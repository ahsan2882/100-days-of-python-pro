import requests


def fetch_questions():
    parameters = {
        'amount': 50,
        'type': 'boolean',
    }
    response = requests.get(
        'https://opentdb.com/api.php', params=parameters)
    response.raise_for_status()
    return response.json()['results']


question_data = fetch_questions()
