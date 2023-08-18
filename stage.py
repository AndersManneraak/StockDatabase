from sql_database import SQLDatabase
from configurations import *
import argparse

def stage(period_id, mapping):
    db = SQLDatabase()
    for table in mapping:
        db.truncate_table(table_name=table,schema='stage')
        insert_stmt = f'insert into stage.{table} select *, {period_id} as period_id from {mapping[table]}'
        db.execute_sql(insert_stmt)
        print('inserted rows to '+table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("period_id", help="periode_id as yyyymmdd.")
    parser.add_argument("mapping", help="stage mapping from configurtation file")
    args = parser.parse_args()
    if args.mapping.lower() == 'full':
        stage(args.period_id,STAGING_FULL_MAPPING)
    if args.mapping.lower() == 'daily':
        stage(args.period_id,STAGING_DAILY_MAPPING)