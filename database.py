#imports
import pandas as pd
import os
import psycopg2
from dotenv import load_dotenv
from functions import sql_to_dataframe, connect
load_dotenv()
#creating a query variable to store our query to pass into the function
query = "SELECT first_name, last_name, email FROM persons"
#creating a list with columns names to pass into the function
column_names = ['first_name','last_name', 'email']
#opening the connection
conn = connect()
#loading our dataframe
df = sql_to_dataframe(conn, query, column_names)
#closing the connection
conn.close()
# Let's see if we loaded the df successfully
df.head()