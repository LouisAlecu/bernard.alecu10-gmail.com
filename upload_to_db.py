import json
import pandas as pd


schema = {'company': [], 'company_address': [], 'company_source': []}
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

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

with open('./sp_file_db/data.json', 'r') as json_file:
    data = json.load(json_file)

flattened_data = []
for i in range(len(data['results']['companies'])):
    flattened_data.append(flatten_json(data['results']['companies'][i]['company']))

# print(flattened_data)

keys = []
for i in range(len(flattened_data)):
    [keys.append(key) for key in list(dict.keys(flattened_data[i])) if key not in keys]

df = pd.DataFrame(flattened_data)
df.to_csv("asdf")

# with open("test.csv.", "w") as f:
#     ls = []
    # for i in range(len(data['results']['companies'])):
    #     for key in keys:
    #         if key not in data['results']['companies'][i]['company']:
    #             data['results']['companies'][i]['company'][key] = None
    #     f.writerow(data['results']['companies'][i]['company'])


    # for i in range(len(keys)):
    #     for j in range(len(flattened_data)):
    #         try:
    #             ls[j] = ls[j].append(flattened_data[j]['company'][keys[i]]) if keys[i] in dict.keys(flattened_data[j]['company'])
    #         except:
    #             ls.append([])








# {'name': '! ! ! 1ST CHOICE ANDROID SMART-PHONE TUTORING, INC.', 'company_number': 'C3517133', 'jurisdiction_code': 'us_ca', 'incorporation_date': '2012-11-02', 
# 'dissolution_date': None, 'company_type': 'DOMESTIC STOCK', 'registry_url': 'https://businessfilings.sos.ca.gov/frmDetail.asp?CorpID=03517133', 
# 'branch': None, 'branch_status': None, 'inactive': True, 'current_status': 'Dissolved', 'created_at': '2012-11-10T03:15:55+00:00', 'updated_at': '2019-12-03T12:53:16+00:00',
#  'retrieved_at': '2019-11-28T01:23:56+00:00', 'opencorporates_url': 'https://opencorporates.com/companies/us_ca/C3517133', 'source_publisher': 'California Secretary of State', 
#  'source_url': 'https://businessfilings.sos.ca.gov/frmDetail.asp?CorpID=03517133', 'source_retrieved_at': '2019-11-28T01:23:56+00:00', 
#  'registered_address_street_address': '420 N MCKINLEY ST #111-182\nCORONA CA 92879', 'registered_address_locality': None, 'registered_address_region': None, 
#  'registered_address_postal_code': None, 'registered_address_country': 'United States', 'registered_address_in_full': '420 N MCKINLEY ST #111-182\nCORONA CA 92879',
#   'restricted_for_marketing': None, 'native_company_number': None}