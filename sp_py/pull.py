from sp_py.api_handler import ApiClient
import pandas as pd
from config import sp_file_db
import json

def main():
    #get request for the /companies/search endpoint
    client = ApiClient('https://api.opencorporates.com/', 'v0.4', api_token=None)
    client.GET_req(endpoint = '/companies/search', params = {'q': 'smart'})
    data = client.get_json()['results']['companies']

    df = pd.DataFrame()
    for company in data:
        df = df.append(company['company'], ignore_index=True)

    df['source'] = df['source'].apply(lambda x: json.dumps(x))
    df['registered_address'] = df['registered_address'].apply(lambda x: json.dumps(x))
    df['inactive'] = df['inactive'].astype(bool)
    df = df.drop('industry_codes', axis=1) #do not want to deal with extra complexity when adding from python to postgres since column is not required
    df = df.drop('previous_names', axis=1)
    df.to_csv(f"{sp_file_db}/data.csv", index=False)

    return df

if __name__ == '__main__':
    main()
