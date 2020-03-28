from sp_py.api_handler import ApiClient
import pandas as pd
# pd.set_option("display.max_rows", 500)
# pd.set_option("display.max_columns", 500)
# pd.set_option("display.width", 1000)


def main():
    #get request for the /companies/search endpoint
    client = ApiClient('https://api.opencorporates.com/', 'v0.4', api_token=None)
    client.GET_req(endpoint = '/companies/search', params = {'q': 'smart'})
    data = client.get_json()['results']['companies']


    flattened_data = []
    for i in range(len(data)):
        flattened_data.append(ApiClient.flatten_json(data[i]['company']))


    df = pd.DataFrame(flattened_data)
    df.to_csv("./sp_file_db/data.csv", index=False)

if __name__ == '__main__':
    main()
