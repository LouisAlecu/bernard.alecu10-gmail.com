import requests
import logging

class ApiClient:
    def __init__(self, url, version, api_token = None):
        self.url = url + version
        print(self.url)
        self.api_token = api_token
        self.response = None
        self.data = {}

    def GET_req(self, endpoint, params):
        url = self.url + endpoint
        params['api_token'] = self.api_token
        print("Request for url: ", url)
        print("Params: ", params)
        self.response = requests.get(url, params=params)
        self.data = self.response.json()
        print("request status: ", self.response.status_code)

    def get_json(self):
        return self.data

    @staticmethod
    def flatten_json(y):
        out = {}
        def flatten(x, name=''):
            if type(x) is dict:
                for a in x:
                    flatten(x[a], name + a + '_')
            elif type(x) is list:
                i = 0
                for a in x:
                    flatten(a, name + str(i) + '_')
                    i += 1
            else:
                out[name[:-1]] = x
        flatten(y)
        return out
