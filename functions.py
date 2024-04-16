import psycopg2
import os
import sys
import pandas as pd

def connect():

   ### Conecta na database ###
    conn = None
    try:
        print('Conectando')
        conn = psycopg2.connect(
                    host=os.environ['DB_PATH'],
                    database=os.environ['DB_NAME'],
                    user=os.environ['DB_USERNAME'],
                    password=os.environ['DB_PASSWORD'])
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print('All good, Connection successful!')
    return conn

def sql_to_dataframe(conn, query, column_names):
   
   # Import data from a PostgreSQL database using a SELECT query 
   
   cursor = conn.cursor()
   try:
      cursor.execute(query)
   except (Exception, psycopg2.DatabaseError) as error:
      print("Error: %s" % error)
      cursor.close()
      return 1
   # The execute returns a list of tuples:
   tuples_list = cursor.fetchall()
   cursor.close()
   # Now we need to transform the list into a pandas DataFrame:
   df = pd.DataFrame(tuples_list, columns=column_names)
   return df
