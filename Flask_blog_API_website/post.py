import requests

API_URL = "https://api.npoint.io/9d2a7ff30100ce7cc232"

class Post:

    def get_data(self):
        #https://www.npoint.io/docs/9d2a7ff30100ce7cc232
        #https://api.npoint.io/9d2a7ff30100ce7cc232
        response = requests.get(API_URL)
        data = response.json()
        return data

