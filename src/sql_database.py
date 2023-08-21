import pandas as pd
import os
from sqlalchemy import *
import sqlalchemy
from configurations import CONNECTION_STRING
from utilities import *

class SQLDatabase:
    def __init__(self):
        #Uses constant connection string. Rewrite or change connection string in configurations.py if switching systems or database.
        self.alc_engine = create_engine(CONNECTION_STRING)

    def execute_sql(self, sql):
        with self.alc_engine.connect() as connection:
            connection.execution_options(isolation_level="AUTOCOMMIT").execute(text(sql))
    
    def fetch_query_result(self, query):
        return pd.read_sql_query(query, self.alc_engine)
    
    def list_tables(self,name_filter=''):
        query = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'" + name_filter
        tables = self.fetch_query_result(query)
        return list(tables['TABLE_NAME'])
    
    def drop_table(self, table_name):
        query = f"DROP TABLE IF EXISTS {table_name}"
        self.execute_sql(query)
    
    def truncate_table(self, table_name, schema='dbo'):
        query = f"TRUNCATE TABLE {schema}.{table_name}"
        self.execute_sql(query)
        print(schema+'.'+table_name + ' has been truncated')

    def table_exists(self, table_name):
        tables = self.list_tables()
        return table_name in tables

    def insert_file_to_table(self, data, table,dtyp, if_exists='append', schema='stock_import'):
        data.to_sql(table, self.alc_engine, if_exists=if_exists, index=False,schema=schema, dtype=dtyp)

    def mulk_insert_file_to_table(self, filepath, table):
        self.execute_sql(f"BULK INSERT dbo.{table} FROM '{filepath}' WITH (KEEPIDENTITY,   FIELDTERMINATOR = ',',   ROWTERMINATOR = '\\n',   FIRSTROW = 2);")
    
    def import_csv_folder_to_database(self,folder_path,include_year=False):
        for file in os.listdir(folder_path):
            if file.endswith(".csv"):
                csv_file_path = os.path.join(folder_path, file)
                table_name = "im_" + os.path.splitext(file)[0]
                
                df = pd.read_csv(csv_file_path)
                #Oracle specific handling of dataframe to avoid bug with pd and sqlalc interaction
                dtyp = self.get_dtyp(df)
                if include_year:
                    df['year'] = folder_path[-4:]
                self.insert_file_to_table(data=df, table=table_name, dtyp=dtyp)
                #self.mulk_insert_file_to_table(filepath=csv_file_path,table=table_name)
                print(f"{csv_file_path} has been successfully inserted into the table: {table_name}") 
    
    def get_dtyp(self,df):
        dtyp = {}
        for column in df.columns:
            dtyp[column] = sqlalchemy.types.VARCHAR(df[column].astype(str).str.len().max())
