import requests
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime as dt
import os

DOTENV_PATH = Path(
    Path(__file__).parent.resolve(),
    '.env'
).resolve()
load_dotenv(DOTENV_PATH)

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
USERNAME = 'ahsan2882'

HEADERS = {
    'X-USER-TOKEN': PIXELA_TOKEN
}

possible_errors = [
    'This user already exist.',
    'This graphID already exist.',
    'Specified pixel not found.'
]


def repeat_request(func, url, json=None, headers=None):
    is_response_success = False
    while not is_response_success:
        response = func(url, json, headers)
        if response['isSuccess']:
            is_response_success = True
        else:
            if response['message'] in possible_errors:
                break

    return response


def post_response(url, json, headers=None):
    return requests.post(
        url=url, json=json, headers=headers).json()


def put_response(url, json, headers):
    return requests.put(
        url=url, json=json, headers=headers).json()


def delete_response(url, json, headers=None):
    return requests.delete(
        url=url, json=json, headers=headers).json()


def create_pixela_user():
    create_user_params = {
        'token': PIXELA_TOKEN,
        'username': USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }
    repeat_request(
        post_response, url=PIXELA_ENDPOINT, json=create_user_params)


# create_pixela_user()


def create_pixela_graph(graph_id: str, graph_name: str, measurement_unit: str, measurement_type: str, graph_color: str):
    create_graph_params = {
        'id': graph_id,
        'name': graph_name,
        'unit': measurement_unit,
        'type': measurement_type,
        'color': graph_color
    }
    repeat_request(
        post_response, url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs", json=create_graph_params, headers=HEADERS)


# create_pixela_graph(graph_id='pyproject1', graph_name='Time Spent on Python Projects',
#                     measurement_unit='minutes', measurement_type='int', graph_color='ajisai')


today = dt.now().strftime('%Y%m%d')


def post_pixela_pixel(date: str, quantity: str, graph_id: str):
    post_pixel_params = {
        'date': date,
        'quantity': quantity
    }
    post_pixel = repeat_request(post_response, url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}",
                                json=post_pixel_params, headers=HEADERS)
    print(post_pixel)


# post_pixela_pixel(date=today,
#                   quantity='900', graph_id='pyproject1')


def updatePixel(date: str, quantity: str, graph_id: str):
    update_pixel_params = {
        'quantity': quantity
    }
    repeat_request(
        put_response, url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date}", json=update_pixel_params, headers=HEADERS)


# updatePixel(date=today, quantity='50', graph_id='pyproject1')


def deletePixel(date: str, graph_id: str):
    repeat_request(
        delete_response, url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date}", headers=HEADERS)


# deletePixel(today, graph_id='pyproject1')
