import csv
import pandas as pd
from sp_py.db_toolbox import connect_to_database
from config import config

# ['branch', 'branch_status', 'company_number', 'company_type', 'created_at', 'current_status', 
# 'dissolution_date', 'inactive', 'incorporation_date', 'industry_codes_0_industry_code_code', 'industry_codes_0_industry_code_code_scheme_id', 
# 'industry_codes_0_industry_code_code_scheme_name', 'industry_codes_0_industry_code_description', 'industry_codes_0_industry_code_uid', 
# 'industry_codes_1_industry_code_code', 'industry_codes_1_industry_code_code_scheme_id', 'industry_codes_1_industry_code_code_scheme_name', 
# 'industry_codes_1_industry_code_description', 'industry_codes_1_industry_code_uid', 'industry_codes_2_industry_code_code', 
# 'industry_codes_2_industry_code_code_scheme_id', 'industry_codes_2_industry_code_code_scheme_name', 'industry_codes_2_industry_code_description', 
# 'industry_codes_2_industry_code_uid', 'jurisdiction_code', 'name', 'native_company_number', 'opencorporates_url', 'previous_names_0_company_name', 
# 'previous_names_0_end_date', 'previous_names_0_start_date', 'registered_address', 'registered_address_country', 'registered_address_in_full', 'registered_address_locality',
#  'registered_address_postal_code', 'registered_address_region', 'registered_address_street_address', 
# 'registry_url', 'restricted_for_marketing', 'retrieved_at', 'source_publisher', 'source_retrieved_at', 'source_terms', 'source_terms_url', 'source_url', 'updated_at']

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


def main():
    with open("./sp_file_db/data.csv", "r") as f:
        reader = csv.reader(f)
        data = [tuple(line) for line in csv.reader(f)]

    data = pd.read_csv("./sp_file_db/data.csv")

    con = connect_to_database(config)
    data[[col for col in schema['company']]].to_sql(
        name="company", con=con.db_con, schema="sp_schema",
    )


# DataFrame.to_sql(self, name: str, con, schema=None, if_exists: str = 'fail', index: bool = True, index_label=None, chunksize=None, dtype=None, method=None) → None
# con.multiple_insert(schema='sp_schema', table='company', columns=[], values=data)
# def multiple_insert(self, schema, table, columns, values):


if __name__ == "__main__":
    main()
