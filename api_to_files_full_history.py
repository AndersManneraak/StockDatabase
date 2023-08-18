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

def main():
    #variables and objects
    YEARS = [datetime.today().year - i for i in range(30)] 
    #folders
    bulk_folder = 'D:/stockdatabase/files/financials/bulk'
    misc_folder = 'D:/stockdatabase/files/misc'
    #------------------------------------ADJUST TO RUN OR SKIP----------------------------------------------
    api_bulk_calls_static = False
    api_bulk_year_calls = False
    api_ticker_calls = True
    #----------------------------------------------------------------------------------------------------------------
    ac = APICaller()
    dh = DataHandler()
    ticker_list = dh.read_csv_to_list(TICKERS_WITH_FINANCIALS_CSV_PATH)
    ticker_list = dh.filter_list_without_substring(ticker_list, '.')
    ticker_list = ['PLTR','GME','AMZN']

    if api_bulk_calls_static:
        ac.set_api_calls(API_BULK_CALLS_STATIC)
        for key in API_BULK_CALLS_STATIC:
            call_bulk(ac,dh,API_BULK_CALLS_STATIC[key][1]+ac.api_key,bulk_folder,key,key)

    if api_bulk_year_calls:
        ac.set_api_calls(API_BULK_YEAR_CALLS)
        for key in API_BULK_YEAR_CALLS:
            for year in YEARS:
                with Timer("time spent on " + key + ' ' + str(year)):
                    for period in ['annual', 'quarter']:
                        call_bulk(ac,dh,API_BULK_YEAR_CALLS[key][1].format(str(year),period) + ac.api_key,bulk_folder+'/'+str(year),key+'_'+period,key)
   
    if api_ticker_calls:
        call_tickers(ac,dh,API_TICKER_CALLS,ticker_list,misc_folder)

if __name__ == '__main__':
    main()