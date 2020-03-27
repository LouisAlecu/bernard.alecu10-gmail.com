import json
from get_data_from_api import ApiClient

client = ApiClient('https://api.opencorporates.com/', 'v0.4', api_token=None)
client.GET_req(endpoint = '/companies/search', params = {'q': 'smart'})

with open('./sp_file_db/data.json', 'w') as f:
    json.dump(client.response.json(), f)

