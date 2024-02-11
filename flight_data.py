class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data, stop_over=0, vie_city="") -> None:
        self.price = data["price"]
        self.departure_airport_code = data["flyFrom"]
        self.departure_city = data["cityFrom"]
        self.arrival_airport_code = data["flyTo"]
        self.arrival_city = data["cityTo"]
        self.departure_date = data["local_departure"].split("T")[0]
        self.departure_time = data["local_departure"].split("T")[1]
        self.return_date = data["route"][1]["local_departure"].split("T")[0]
        self.return_time = data["route"][1]["local_departure"].split("T")[1]
        self.stop_over = stop_over
        self.vie_city = vie_city
        self.check_stop_over(data)

    def check_stop_over(self, data):
        if self.stop_over == 1:
            self.return_date = data["route"][2]["local_departure"].split("T")[0]
            self.return_time = data["route"][2]["local_departure"].split("T")[1]
