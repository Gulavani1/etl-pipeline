import psycopg2
import pandas as pd

def connect_to_redshift(dbname, host, port, user, password):
    """Method that connects to redshift. This gives a warning so will look for another solution"""

    connect=psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("connection to redshift made")

    return connect

def extract_transactional_data(dbname, host, port, user, password):
    #connect to redshift

    connect = connect_to_redshift(dbname, host, port, user, password)

    ## query that extract transactional data and carry out the transformation tasks

    query = """
    select ot.invoice,
    ot.stock_code,
    ot.quantity,
    case when sd.description is null then 'UNKNOWN' else sd.description end as description,
    cast(ot.invoice_date as datetime)as invoice_date,
    ot.price,
    ot.customer_id,
    ot.country
    from bootcamp.online_transactions ot
    left join (select *
              from bootcamp.stock_description
              where description <> '?') sd on ot.stock_code = sd.stock_code
    where ot.customer_id <> ''
     and ot.stock_code not in ('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
    """
    # storing this data we have extracted as a dataframe
    online_trans_transformed = pd.read_sql(query, connect)

    print("The shape of extracted and transformed data is:", online_trans_transformed.shape)

    return online_trans_transformed