create database sp;
\c sp;

create schema sp_schema;

drop table if exists sp_schema.company cascade;
create table sp_schema.company (
    company_name                 text
    ,company_jurisdiction_code   varchar(10)
    ,company_number              text
    ,incorporation_date          timestamp without time zone
    ,dissolution_date            timestamp without time zone
    ,company_type                text
    ,registry_url                text
    ,branch                      text
    ,branch_status               text
    ,inactive                    boolean
    ,current_status              text
    ,created_at                  timestamptz
    ,updated_at                  timestamptz
    ,retrieved_at                timestamptz
    ,opencorporates_url          text
    ,previous_names              text[]
    ,source                      jsonb default '{}'::jsonb
    ,registered_address          jsonb default '{}'::jsonb
    ,registered_address_in_full  jsonb default '{}'::jsonb
    ,industry_codes              jsonb[]
    ,restricted_for_marketing    boolean
    ,native_company_number       text

    ,primary key(company_name, company_jurisdiction_code)
);

create table sp_schema.company_address (
    id                              serial not null primary key
    ,company_name                   text not null references sp_schema.company(company_name)
    ,company_jurisdiction_code      text not null references sp_schema.company(company_jurisdiction_code)
    ,street_address                 text
    ,locality                       text
    ,region                         text
    ,postal_code                    text
    ,country                        text
);

create table sp_schema.company_source (
    id                              serial not null primary key
    ,company_name                   text not null references sp_schema.company(company_name)
    ,company_jurisdiction_code      text not null references sp_schema.company(company_jurisdiction_code)
    ,publisher                      text
    ,url                            text
    ,retrieved_at                   timestamptz
    ,terms                          text
    ,terms_url                      text
);
