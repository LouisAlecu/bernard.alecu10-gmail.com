import csv
import numpy as np
import pandas as pd
from db_toolbox import connect_to_database
from config import config, sp_file_db
import json
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

schema = {
    'company': [
        'name',
        'jurisdiction_code',
        'company_number',
        'incorporation_date',
        'dissolution_date',
        'company_type',
        'registry_url',
        'branch',
        'branch_status',
        'inactive',
        'current_status',
        'created_at',
        'updated_at',
        'retrieved_at',
        'opencorporates_url',
        'restricted_for_marketing',
        'native_company_number',
    ]
}

def clean_none_values(dictionary):
    clean_dict = {}
    print(dictionary)
    for k,v in dictionary:
        if v is not None:
            clean_dict[k] = v
    return clean_dict


def main():
    with open(f"{sp_file_db}/data.csv", "r") as f:
        reader = csv.reader(f)
        data = [tuple(line) for line in csv.reader(f)]

    data = pd.read_csv(f"{sp_file_db}/data.csv")

    con = connect_to_database(config)
    data.to_sql(name="company", schema='sp_schema', con=con.engine, if_exists='append', index=False)


if __name__ == "__main__":
    main()
