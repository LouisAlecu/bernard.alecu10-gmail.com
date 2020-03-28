import json
import pandas as pd
from sp_py.db_toolbox import connect_to_database

schema = {'company': [], 'company_address': [], 'company_source': []}
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)


with open('./sp_file_db/data.json', 'r') as json_file:
    data = json.load(json_file)

flattened_data = []
for i in range(len(data['results']['companies'])):
    flattened_data.append(flatten_json(data['results']['companies'][i]['company']))


df = pd.DataFrame(flattened_data)
df.to_csv("asdf")

