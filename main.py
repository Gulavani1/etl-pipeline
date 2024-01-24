import os
# this library is being used to read from the .env file
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicates
from src.load_data_to_s3 import df_to_s3
start_time = datetime.now()


## reading the variables from the .env file
user = os.getenv("user")
host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")
password = os.getenv("password")
aws_access_key_id=os.getenv("aws_access_key_id")
aws_secret_access_key=os.getenv("aws_secret_access_key_id")

#step 1:extract data
ot_transformed = extract_transactional_data(dbname, host, port, user, password)

#identify and remove duplicates

#online_trans_transformed.drop_duplicates(keep='first',inplace= True)
#print(online_trans_transformed.shape)

# step 2: identify and remove duplicate
ot_wout_duplicates = identify_and_remove_duplicates(ot_transformed)

# step 3: load data to s3
key="transformations_final/pg_online_trans_transformed.pkl"
s3_bucket="sep-bootcamp"

df_to_s3(ot_wout_duplicates, key, s3_bucket, aws_access_key_id, aws_secret_access_key)

# if you want to you can calculate
execution_time = datetime.now() - start_time
print(f"Total execution time (hh:mm:ss) {execution_time}")

