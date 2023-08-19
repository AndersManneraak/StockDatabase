from utilities import *
import pandas as pd
import pymssql as pymssql
from configurations import *
from sqlalchemy import create_engine
from sql_database import SQLDatabase
import os
import argparse

# Connection parameters and connection
db = SQLDatabase()
bulk = 'D:/stockdatabase/files/financials/bulk'
misc = 'D:/stockdatabase/files/misc'
general = 'D:/stockdatabase/files/general'
daily = 'D:/stockdatabase/files/daily'
   
def full_folder_import(path,include_year=False):
    db.import_csv_folder_to_database(path,include_year=include_year)

subfolders = [ f.name for f in os.scandir(bulk) if f.is_dir() ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mapping", help="folders to import. daily or full")
    args = parser.parse_args()
    if args.mapping.lower() == 'full':
        with Timer("Bulk with period"):
            for table in API_BULK_YEAR_CALLS:
                table_y = 'im_'+table+'_annual'
                table_q = 'im_'+table+'_quarter'
                #db.truncate_table(table_y)
                #db.truncate_table(table_q)
            for subfolder in subfolders:
                with Timer("Year " + subfolder + 'inserted'):
                    full_folder_import(bulk+'/'+subfolder)
        with Timer("Bulk other"):
            full_folder_import(bulk)
        with Timer("General"):
            full_folder_import(general)
        with Timer("misc"):
            full_folder_import(misc)
    if args.mapping.lower() == 'daily':
        with Timer("daily"):
            full_folder_import(daily)
    else:
        print("enter daily or full as argument to the file")