# Flight search app
A simple application for finding cheap flights (Python, API, OOP)
## How it works
The application uses the Sheety API to get information from Google Sheets about flight destinations (city, IATA code, lowest price) and also to get information about users (name, email). The Tequila API is used to search for the cheapest tickets for a flight from London to all cities in the table. If the ticket price is lower than indicated in the table, all users receive a message by e-mail.