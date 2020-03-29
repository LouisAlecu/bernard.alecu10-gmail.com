from api_handler import ApiClient
import re 

def test_GET_company():
    client = ApiClient("https://api.opencorporates.com", "v0.4", api_token=None)
    client.GET_companies_search(params={"q": "smart"})
    data = client.get_json()["results"]["companies"]

    assert (len(data) == 30)


def test_GET_companies_search():
    client = ApiClient("https://api.opencorporates.com", "v0.4", api_token=None)
    client.GET_company('pl', '0000011037')
    data = client.get_json()
    
    assert (client.get_request_status() == 200 and len(data) != 0)
