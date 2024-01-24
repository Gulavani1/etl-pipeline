# ETL Pipeline v1

# Introduction
This code contains the steps to build an ETL pipeline that carries
-Extract 400k transactions from Redshift
-Identifies and remove duplicates
-Loads the transformed data to a s3 bucket

## Reqiurements
The minimum requirements:
-Python 3+

## Instructions on how to execute the code

1.Clone the repository and go to week19 folder

2. Install the libraries that they need to run main.py
pip3 install -r requirements.txt

3. 3.Copy the .env.copy file to .envand fill out the environment variabls.

4.Run the main.py script Mac users:

python3 main.py

Window users:

python main.py