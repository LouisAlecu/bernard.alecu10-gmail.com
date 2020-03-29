create database sp;
\c sp;

create schema sp_schema;


-- branch,branch_status,company_number,company_type,created_at,current_status,dissolution_date,inactive,
-- incorporation_date,industry_codes,jurisdiction_code,name,native_company_number,
-- opencorporates_url,previous_names,registered_address,registered_address_in_full,registry_url,restricted_for_marketing,retrieved_at,source,updated_at

drop table if exists sp_schema.company;
create table sp_schema.company (
    id                           serial not null primary key
    ,name                        text
    ,jurisdiction_code           varchar(10)
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
    ,source                      jsonb default '{}'::jsonb
    ,registered_address          jsonb default '{}'::jsonb
    ,registered_address_in_full  text
    ,opencorporates_url          text
    ,restricted_for_marketing    boolean
    ,native_company_number       text

    ,unique(name, jurisdiction_code)

);


drop table if exists sp_schema.registered_address;
create table sp_schema.registered_address (
    id                              serial not null primary key
    ,name                           text not null
    ,jurisdiction_code              text not null
    ,street_address                 text
    ,locality                       text
    ,region                         text
    ,postal_code                    text
    ,country                        text

    ,foreign key(name, jurisdiction_code) references sp_schema.company(name, jurisdiction_code)
);

drop table if exists sp_schema.source;
create table sp_schema.source (
    id                              serial not null primary key
    ,name                           text not null
    ,jurisdiction_code              text not null
    ,publisher                      text
    ,url                            text
    ,retrieved_at                   timestamptz
    ,terms                          text
    ,terms_url                      text

    ,foreign key(name, jurisdiction_code) references sp_schema.company(name, jurisdiction_code)
);
