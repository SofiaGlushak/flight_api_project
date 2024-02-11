import smtplib
import os

MY_ADDRESS = os.environ.get("MY_ADDRESS")
PASSWORD = os.environ.get("MY_PASSWORD")


class NotificationManager:

    def send_email(self, users, flight):
        body_text = f"Only {flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to {flight.arrival_city}-{flight.arrival_airport_code}, from {flight.departure_date} to {flight.return_date}."
        if flight.stop_over == 1:
            body_text += f"\nFlight has 1 stop over, via {flight.vie_city}."
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_ADDRESS, password=PASSWORD)
            for user in users:
                connection.sendmail(from_addr=MY_ADDRESS,
                                    to_addrs=user["email"],
                                    msg=f"Subject:Low price alert!\n\n{body_text}")
