import requests
from dotenv import load_dotenv
import os
from pathlib import Path
from datetime import datetime as dt

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()
load_dotenv(DOTENV_PATH)

GENDER = 'male'
WEIGHT_KG = 102
HEIGHT_CM = 180
AGE = 23
NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
NUTRITIONIX_APP_KEY = os.getenv('NUTRITIONIX_APP_KEY')

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2"
SHEETY_AUTH_KEY = os.getenv('SHEETY_AUTH_KEY')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_HEADER = {
    'Authorization': f'Bearer {SHEETY_AUTH_KEY}'
}

exercise_text = input("Tell me which exercises you did: ")

exersise_headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_APP_KEY,
    'x-remote-user-id': '0',
}

excersise_params = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}
nutritionix_response = requests.post(url=f"{NUTRITIONIX_ENDPOINT}/natural/exercise",
                                     headers=exersise_headers, json=excersise_params).json()['exercises']

for exercise in nutritionix_response:
    sheety_data = {
        'workout': {
            'date': dt.now().strftime('%d/%m/%Y'),
            'time': dt.now().strftime('%X'),
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }
    sheety_response = requests.post(
        url=SHEETY_ENDPOINT, headers=SHEETY_HEADER, json=sheety_data
    ).json()
