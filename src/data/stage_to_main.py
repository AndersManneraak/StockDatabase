from sql_database import SQLDatabase
from configurations import *

if __name__ == "__main__":
    db = SQLDatabase()
    db.insert_data_from_views_to_tables(MAIN_MAPPING, truncate=True,schema='main')