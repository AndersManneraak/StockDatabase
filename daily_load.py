from api_to_files_daily import *
from files_to_im_tables import *
from configurations import *
from stage import *
from update_universe import *
import argparse

def daglast():
    parser = argparse.ArgumentParser()
    parser.add_argument("period_id", help="periode_id as yyyymmdd.")
    args = parser.parse_args()
    to_files_daily()
    full_folder_import(daily)
    stage(args.period_id,STAGING_DAILY_MAPPING)
    update_universe(UNIVERSE)
    update_portfolio(PORTFOLIO)

if __name__ == "__main__":
    daglast()
    