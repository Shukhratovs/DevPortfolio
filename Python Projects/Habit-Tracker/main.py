import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "Humoyun0050@"
USERNAME = "shukhratov"
GRAPH_ID = "graph1"

today = datetime(year=2024, month=1, day=3)
DATE = today.strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Learning Graph",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": DATE,
    "quantity": input("How long did you study today?: "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixel_creation_endpoint}/{DATE}"

update_pixel_config = {
    "quantity": "50",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text

delete_endpoint = f"{pixel_creation_endpoint}/{DATE}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
