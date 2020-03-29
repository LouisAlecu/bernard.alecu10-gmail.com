import requests
import logging

class ApiClient:
    def __init__(self, root_endpoint, version, api_token = None):
        self._root_endpoint = root_endpoint
        self._version = version
        self._api_token = api_token
        self._response = None
        self._data = {}

    def GET_companies_search(self, params):
        url = self._url('companies', 'search')
        print(url)
        params['api_token'] = self._api_token
        self._response = requests.get(url, params=params)
        print("request status: ", self._response.status_code)
        self._data = self._response.json()

    def GET_company(self, jurisdiction_code, company_number, params={}):
        url = self._url('companies', jurisdiction_code, company_number)
        print(url)
        params['api_token'] = self._api_token
        self._response = requests.get(url, params=params)
        print("request status: ", self._response.status_code)
        self._data = self._response.json()

    def get_json(self):
        return self._data

    def _url(self, *args):
        return f"{self._root_endpoint}/{self._version}/{'/'.join(args)}"


