import requests
import logging


class ApiClient:
    def __init__(self, root_endpoint, version, api_token=None):
        """
        Initialize the attributes based on the api information
        """
        self._root_endpoint = root_endpoint
        self._version = version
        self._api_token = api_token
        self._response = None
        self._data = {}
        self._last_req_status = None
        self._api_limit = 50

        if self._api_token:
            self._is_authenticated = True
        else:
            self._is_authenticated = False

    def GET_companies_search(self, params):
        """ 
        GET request to the /companies/search endpoint
        """
        url = self._url("companies", "search")
        print(url)
        if "api_token" not in params:
            params["api_token"] = self._api_token
        self._response = requests.get(url, params=params)
        self._last_req_status = self._response.status_code
        if self._error_handling():
            self._data = self._response.json()

    def GET_company(self, jurisdiction_code, company_number, params={}):
        """ 
        GET request to the /companies/:jurisdiction:/:company_number: endpoint
        """
        url = self._url("companies", jurisdiction_code, company_number)
        print(url)
        if "api_token" not in params:
            params["api_token"] = self._api_token
        self._response = requests.get(url, params=params)
        self._last_req_status = self._response.status_code
        if self._error_handling():
            self._data = self._response.json()

    def GET_custom_endpoint(self, *args, params={}):
        """
        Since I have not implemented a method for each endpoint, I created this
        to simulate them.
        """
        url = self._url(*args)
        print(url)
        if "api_token" not in params:
            params["api_token"] = self._api_token
        print(params["api_token"])
        self._response = requests.get(url, params=params)
        self._last_req_status = self._response.status_code
        self._error_handling()

    def _error_handling(self):
        if self._last_req_status == 200:
            print("Request executed successfully.")
            return True
        elif self._last_req_status == 403:
            print("You exceeded the requests limit.")
        elif self._last_req_status == 401:
            print("Unauthorized access. Probably invalid credentials.")
        elif self._last_req_status == 400:
            print("Bad request.")
        else:
            print("The response code is {self._last_req_status}")
        return False

    def _url(self, *args):
        return (
            f"{self._root_endpoint}/{self._version}/{'/'.join(args)}"
            if args
            else f"{self._root_endpoint}"
        )

    def upload_api_token(self, api_token):
        """
        Functionality to change the api token.
        """
        print(
            "This will try a request with your token to check if it is valid, so the last request status will change."
        )
        # The next is an endpoint that requires credentials.
        self.GET_custom_endpoint(
            "companies",
            "us_nj",
            "0400549703",
            "events",
            params={"api_token": api_token},
        )
        if self._last_req_status == 200:
            self._is_authenticated = True
        else:
            print(
                "Token might be invalid, code {self._last_req_status} returned. Check codes meaning in the documentation."
            )
            self._is_authenticated = False

    def get_request_status(self):
        return self._last_req_status

    def get_json(self):
        return self._data

    def get_response_object_itself(self):
        return self._response
