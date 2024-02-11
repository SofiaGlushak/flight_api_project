from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import datetime as dt

data_manager = DataManager()
flight_search = FlightSearch()
flights = []

sheet_data = data_manager.get_sheet_data()
for city in sheet_data:
    if city['iataCode'] == '':
        city['iataCode'] = flight_search.search_loc(city['city'])
        data_manager.put_row(city)

data_manager.all_data = sheet_data

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
tomorrow = tomorrow.strftime("%d/%m/%Y")
last_date = dt.datetime.now() + dt.timedelta(days=180)
last_date = last_date.strftime("%d/%m/%Y")

for city in sheet_data:
    data = flight_search.search_flights(city['iataCode'], tomorrow, last_date)
    if data is None:
        data = flight_search.search_flights(city['iataCode'], tomorrow, last_date, max_stops=2)
        if data is None:
            continue
        else:
            flight = FlightData(data, stop_over=1, vie_city=data["route"][0]["cityTo"])
    else:
        flight = FlightData(data)
    print(f"{flight.arrival_city}: {flight.price}")
    if city["lowestPrice"] > flight.price:
        users = data_manager.get_all_users()
        notification_manager = NotificationManager()
        notification_manager.send_email(users, flight)
