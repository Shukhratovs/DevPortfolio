from pprint import pprint
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "iq0RgKAuhy7-GRTV-ewoA1gHDlZ92w3i"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        data = response.json().get("data")

        if not data:
            # Try with 1 stopover if no direct flights are found
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json().get("data")

            if not data:
                # No flights found with the given parameters
                print(f"No flights found for {origin_city_code} to {destination_city_code}")
                return None

        # Assuming the first result is the desired one
        flight_info = data[0]

        # Create a FlightData object from the flight information
        flight_data = FlightData(
            price=flight_info["price"],
            origin_city=flight_info["route"][0]["cityFrom"],
            origin_airport=flight_info["route"][0]["flyFrom"],
            destination_city=flight_info["route"][0]["cityTo"],
            destination_airport=flight_info["route"][0]["flyTo"],
            out_date=flight_info["route"][0]["local_departure"].split("T")[0],
            return_date=flight_info["route"][1]["local_departure"].split("T")[0]
        )

        return flight_data
