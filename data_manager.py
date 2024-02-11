import requests
from pprint import pprint
import os

END_POINT_PRICES = os.environ.get("PRICES_URL")
END_POINT_USERS = os.environ.get("USERS_URL")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.all_data = []

    def get_sheet_data(self):
        self.all_data = requests.get(url=END_POINT_PRICES).json()["prices"]
        return self.all_data

    def print_data(self):
        pprint(self.all_data)

    def put_row(self, city):
        id_row = city['id']
        code = city['iataCode']
        body = {
            'price': {
                'iataCode': code
            }
        }
        response = requests.put(url=f"{END_POINT_PRICES}/{id_row}", json=body)
        print(response.text)

    def get_all_users(self):
        response = requests.get(url=END_POINT_USERS)
        result = response.json()["users"]
        return result
