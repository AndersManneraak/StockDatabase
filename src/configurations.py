
#--------------------CONNECTIONS------------------
#passwords
FMPAPI = '28f8e0695d72e13bac21ddedc70bb460'
#Connections
SERVER = 'Anders_Desktop'
DATABASE = 'Stocks'
ORCL_USER = 'stock_import'
pw = 'Warlordmanrock95'
host = 'localhost'
service_name = 'orcl'
port = '1521'
#CONNECTION_STRING = f'mssql+pyodbc://{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
CONNECTION_STRING = f'oracle://{ORCL_USER}:{pw}@{host}:{port}/?service_name={service_name}'

#----------------------TABLE - VIEW - MAPPING -----------------------------------------------------------
STAGING_FULL_MAPPING= {
    "st_all_tickers": "dbo.v_im_alltickers",
    "st_metrics_annual": "dbo.v_im_metrics_annual",
    "st_daily_losers": "dbo.v_im_losers",
    "st_daily_gainers": "dbo.v_im_gainers",
    "st_daily_commodities": "dbo.v_im_commodities",
    "st_daily_price": "dbo.v_im_daily_price",
    "st_daily_indexes": "dbo.v_im_daily_indexes"
    }
STAGING_DAILY_MAPPING={
    "st_daily_losers": "dbo.v_im_losers",
    "st_daily_gainers": "dbo.v_im_gainers",
    "st_daily_commodities": "dbo.v_im_commodities",
    "st_daily_price": "dbo.v_im_daily_price",
    "st_daily_indexes": "dbo.v_im_daily_indexes",
    "st_insider_trading": "dbo.v_im_insider_trading"
}
MAIN_MAPPING= {
    "all_tickers": "dbo.v_st_alltickers"
    }
#--------------------API URLs----------------------
#--------------------DAILY-------------------------
API_DAILY_BULK_CALLS = {
    "gainers": ['j',"https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey="],
    "losers": ['j',"https://financialmodelingprep.com/api/v3/stock_market/losers?apikey="],
    "commodities": ['j',"https://financialmodelingprep.com/api/v3/quotes/commodity?apikey="],
    "daily_price_nyse": ['j',"https://financialmodelingprep.com/api/v3/quotes/nyse?apikey="],
    "daily_price_nasdaq": ['j',"https://financialmodelingprep.com/api/v3/quotes/nasdaq?apikey="],
    "indexes": ['j',"https://financialmodelingprep.com/api/v3/quotes/index?apikey="]
}
#-------------------HISTORICAL OR OCCASIONAL---------------------------
API_BULK_YEAR_CALLS = {
    "income_statement_bulk": ['c',"https://financialmodelingprep.com/api/v4/income-statement-bulk?year={}&period={}&apikey="],
    "balance_sheet_bulk": ['c',"https://financialmodelingprep.com/api/v4/balance-sheet-statement-bulk?year={}&period={}&apikey="],
    "cash_flow_bulk": ['c',"https://financialmodelingprep.com/api/v4/cash-flow-statement-bulk?year={}&period={}&apikey="],
    "ratios_bulk": ['c',"https://financialmodelingprep.com/api/v4/ratios-bulk?year={}&period={}&apikey="],
    "key_metrics_bulk": ['c',"https://financialmodelingprep.com/api/v4/key-metrics-bulk?year={}&period={}&apikey="],
    "profile_all_bulk": ['c',"https://financialmodelingprep.com/api/v4/profile/all?apikey="],
}
API_BULK_CALLS_STATIC = {
    "stock_peers_bulk": ['c',"https://financialmodelingprep.com/api/v4/stock_peers_bulk?apikey="],
    "rating_bulk": ['c',"https://financialmodelingprep.com/api/v4/rating-bulk?apikey="],
    "dcf_bulk": ['c',"https://financialmodelingprep.com/api/v4/dcf-bulk?apikey="],
    "scores_bulk": ['c',"https://financialmodelingprep.com/api/v4/scores-bulk?apikey="],
    "delisted": ['j',"https://financialmodelingprep.com/api/v3/delisted-companies?page=0&apikey="],
    "historical_sector_performance": ['j',"https://financialmodelingprep.com/api/v3/historical-sectors-performance?limit=500&apikey="]
}

API_TICKER_CALLS = {
    "insider_trading": ['j',"https://financialmodelingprep.com/api/v4/insider-trading?transactionType=P-Purchase,S-Sale&symbol={}&apikey="],
    "stock_peers": ['j',"https://financialmodelingprep.com/api/v4/stock_peers?symbol={}&apikey="],
    "key_executives": ['j',"https://financialmodelingprep.com/api/v3/key-executives/{}?apikey="],
    "dividend": ['j',"https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{}?apikey="],
    "price_target_consensus": ['j',"https://financialmodelingprep.com/api/v4/price-target-consensus?symbol={}&apikey="],
    "price_target": ['j',"https://financialmodelingprep.com/api/v4/price-target?symbol={}&apikey="],
    "dcf_historical_y": ['j',"https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow-statement/{}?apikey="],
    "dcf_historical_q": ['j',"https://financialmodelingprep.com/api/v3/historical-discounted-cash-flow-statement/{}?period=quarter&apikey="]
}

API_DAILY_TICKER_CALLS = {
    "insider_trading": ['j',"https://financialmodelingprep.com/api/v4/insider-trading?transactionType=P-Purchase,S-Sale&symbol={}&apikey="]
}


#----------------------------------------------------------------------------FILES--------------------------------------------------
TICKERS_WITH_FINANCIALS_CSV_PATH = 'E:/stockdatabase/files/general/tickers_with_financials.csv'
SP500_TICKERS = 'E:/stockdatabase/files/general/sp500_constituent.csv'

UNIVERSE = ['GME','AMZN','AAPL','PLTR','NNBR','CYTH','FRP','WFC','WAL','CTRA',
            'GEO','META','JD','BABA','SIG','NYCB','ZM','COF','SBSW','LILAK','CI','COHR',
            'NOV','DVN','PACW','FRCB','HBAN','REAL','OVV','PBF','UFI','GIII','OLN',
            'TSE','SD','ILMN','CVGI','MAC','BZH','AR','ROIC','OMI', 'PUMP','FTK','AA',
            'PTEN','MAXR','MEOH','NGS']

PORTFOLIO = {'cash_in_usd': 2500, 'gme': 50, 'real': 450, 'nnbr': 500, 'jd': 20}