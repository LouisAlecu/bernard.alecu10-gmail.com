create database sp;
\c sp;

create schema sp_schema;

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
    ,opencorporates_url          text
    ,restricted_for_marketing    boolean
    ,native_company_number       text

    ,unique(id, name, jurisdiction_code)

);

drop table if exists sp_schema.registered_address;
create table sp_schema.registered_address (
    id                              serial not null primary key
    ,company_id                     integer
    ,name                           text not null
    ,jurisdiction_code      text not null
    ,street_address                 text
    ,locality                       text
    ,region                         text
    ,postal_code                    text
    ,country                        text

    ,foreign key(company_id, name, jurisdiction_code) references sp_schema.company(id, name, jurisdiction_code)
);

drop table if exists sp_schema.source;
create table sp_schema.source (
    id                              serial not null primary key
    ,company_id                     integer
    ,name                           text not null
    ,jurisdiction_code              text not null
    ,publisher                      text
    ,url                            text
    ,retrieved_at                   timestamptz
    ,terms                          text
    ,terms_url                      text

    ,foreign key(company_id, name, jurisdiction_code) references sp_schema.company(id, name, jurisdiction_code)
);
