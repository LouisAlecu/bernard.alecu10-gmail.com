import requests

class ApiClient:
    def __init__(self, url, version, api_token = None):
        self.url = url + version
        print(self.url)
        self.api_token = api_token
        self.response = None

    def GET_req(self, endpoint, params):
        url = self.url + endpoint
        params['api_token'] = self.api_token
        print("Request for url: ", url)
        print("Params: ", params)
        self.response = requests.get(url, params=params)
        print("request status: ", self.response.status_code)

