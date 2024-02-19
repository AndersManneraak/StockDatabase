from datetime import *
from configurations import *
from utilities import Timer
from apicaller import APICaller
from datahandler import DataHandler

def call_bulk(ac,dh,api,folder,filename,key):
    if ac.api_calls[key][0] == 'c':
        df = ac.get_csv_data(api)
    else:
        json = ac.get_json_data(api)
        df = dh.json_to_df(json)
    dh.set_output_dir(folder)
    dh.save_data_to_csv(df,filename)

def call_tickers(ac,dh,api_calls,tickers,folder):
    dh.set_output_dir(folder)
    ac.set_api_calls(api_calls)
    with Timer('Time spent on getting files to: ' + folder):
        for key in api_calls:
            with Timer('Time spent on: ' + key):
                df_list = []
                for ticker in tickers:
                    url = api_calls[key][1]+ac.api_key
                    url = url.format(ticker)
                    json = ac.get_json_data(url)
                    df = dh.json_to_df(json)
                    df_list.append(df)
                dh.set_output_dir(folder)
                dh.df_list_to_file(df_list,folder+'/' + key+'.csv')

def to_files_daily():
    daily_folder = 'E:/stockdatabase/files/daily'
    ac = APICaller()
    dh = DataHandler()
    ac.set_api_calls(API_DAILY_BULK_CALLS)
    for key in ac.api_calls:
        call_bulk(ac,dh,API_DAILY_BULK_CALLS[key][1]+ac.api_key,daily_folder,key,key)
    
    ac.set_api_calls(API_DAILY_TICKER_CALLS)
    call_tickers(ac,dh,API_DAILY_TICKER_CALLS,UNIVERSE,daily_folder)

  

if __name__ == '__main__':
    to_files_daily()