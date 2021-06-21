import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=4, day=29)
format_today = today.strftime("%Y%m%d")

information = {
    "date": format_today,
    "quantity": "15.5"
}
#
# response = requests.post(url=pixel_create_endpoint, headers=headers, json=information)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{format_today}"

update_data = {
    "quantity": "10"
}

response = requests.put(url=update_pixel_endpoint, headers=headers, json=update_data)
print(response.text)
