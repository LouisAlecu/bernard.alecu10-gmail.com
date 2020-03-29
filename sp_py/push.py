import csv
import numpy as np
import pandas as pd
from db_toolbox import connect_to_database
from config import config, sp_file_db
import json
pd.options.mode.chained_assignment = None

def flatten_df(df, col):
    for i, row in df.iterrows():
        json_col = json.loads(row[col])["values"]
        if json_col:
            for k, v in json_col.items():
                df.loc[i, k] = v
    df = df.drop(col, axis=1)

    return df


def main():
    with open(f"{sp_file_db}/data.csv", "r") as f:
        reader = csv.reader(f)
        company = [tuple(line) for line in csv.reader(f)]

    company = pd.read_csv(f"{sp_file_db}/data.csv")

    registered_address = flatten_df(
        company[["jurisdiction_code", "company_number", "registered_address"]],
        "registered_address",
    )

    source = flatten_df(
        company[["jurisdiction_code", "company_number", "source"]], "source"
    )

    con = connect_to_database(config)
    company.to_sql(
        name="company",
        schema="sp_schema",
        con=con.engine,
        if_exists="append",
        index=False,
    )
    registered_address.to_sql(
        name="registered_address",
        schema="sp_schema",
        con=con.engine,
        if_exists="append",
        index=False,
    )
    source.to_sql(
        name="source",
        schema="sp_schema",
        con=con.engine,
        if_exists="append",
        index=False,
    )


if __name__ == "__main__":
    main()
