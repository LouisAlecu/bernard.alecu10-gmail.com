from sp_py.api_handler import ApiClient
import pandas as pd
from sp_py.db_toolbox import get_config
import json
import sys


def get_ultimate_beneficial_owners(pd_series, client):
    client.GET_company(pd_series.jurisdiction_code, pd_series.company_number)
    ubo = client.get_json()["results"]["company"]["ultimate_beneficial_owners"]
    pd_series["ultimate_beneficial_owners"] = (
        json.dumps({"values": ubo}) if ubo else json.dumps({"values": []})
    )

    return pd_series


def main():
    config, sp_file_db = get_config()
    client = ApiClient("https://api.opencorporates.com", "v0.4", api_token=None)
    client.GET_companies_search(params={"q": "smart"})
    data = client.get_json()["results"]["companies"]

    df = pd.DataFrame()
    for company in data:
        df = df.append(company["company"], ignore_index=True)

    df["source"] = df["source"].apply(
        lambda x: json.dumps({"values": x}) if x else json.dumps({"values": []})
    )
    df["registered_address"] = df["registered_address"].apply(
        lambda x: json.dumps({"values": x}) if x else json.dumps({"values": []})
    )
    df["previous_names"] = df["previous_names"].apply(
        lambda x: json.dumps({"values": x}) if x else json.dumps({"values": []})
    )
    df["industry_codes"] = df["industry_codes"].apply(
        lambda x: json.dumps({"values": x} if x else json.dumps({"values": []}))
    )
    df["inactive"] = df["inactive"].astype(bool)

    df = df.head(10)

    client = ApiClient("https://api.opencorporates.com", "v0.4", api_token=None)
    df["ultimate_beneficial_owners"] = ""
    df[["jurisdiction_code", "company_number", "ultimate_beneficial_owners"]] = df[
        ["jurisdiction_code", "company_number", "ultimate_beneficial_owners"]
    ].apply(lambda x: get_ultimate_beneficial_owners(x, client), axis=1)
    df.to_csv(f"{sp_file_db}/data.csv", index=False)

    return df


if __name__ == "__main__":
    main()
