import requests
import os

API_KEY = os.environ.get("API_KEY")
END_POINT = "https://api.tequila.kiwi.com"
ORIGIN_CITY_IATA = "LON"


class FlightSearch:
    def search_loc(self, city_name):
        header = {
            "apikey": API_KEY
        }
        parameters = {
            "term": city_name,
            "location_types": "city",
            "locale": "en-US",
            "limit": 10,
            "active_only": True
        }
        response = requests.get(url=f"{END_POINT}/locations/query", headers=header, params=parameters)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def search_flights(self, city_code, tomorrow, last_date, max_stops=0):
        header = {
            "apikey": API_KEY
        }
        parameters = {
            "fly_from": ORIGIN_CITY_IATA,
            "fly_to": city_code,
            "date_from": tomorrow,
            "date_to": last_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": max_stops
        }
        response = requests.get(url=f"{END_POINT}/v2/search", headers=header, params=parameters)
        try:
            result = response.json()["data"][0]
        except IndexError:
            result = None
        return result
