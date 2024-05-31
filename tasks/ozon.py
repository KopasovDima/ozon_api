import requests
from constants import OZON_URL
from tasks.init_celery import celery
import json


@celery.task
def get_actions(client_id: str, api_key: str):
    ozon_response = requests.get(f'{OZON_URL}/actions', headers={'Client-Id': client_id, 'Api-Key': api_key})
    file_name = 'actions.json' if ozon_response.status_code == 200 else 'actions_error.json'
    with open(file_name, 'w') as file:
        file.write(json.dumps(ozon_response.json()))
