import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    def get(self, endpoint):
        return requests.get(self.base_url + endpoint)
    def post(self, endpoint, json):
        return requests.post(f"{self.base_url}{endpoint}", json=json)
    def put(self, endpoint, json):
        return requests.put(f"{self.base_url}{endpoint}", json=json)
    def delete(self, endpoint):
        return requests.delete(self.base_url + endpoint)