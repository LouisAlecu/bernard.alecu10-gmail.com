import json

with open('./data/data.json', 'r') as json_file:
    data = json.load(json_file)

x=data['results']['companies']
print(len(x))
print(x[0])