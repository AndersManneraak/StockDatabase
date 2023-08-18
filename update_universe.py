from sql_database import SQLDatabase
from configurations import *

def update_universe(universe):
    db = SQLDatabase()
    db.truncate_table(table_name='universe',schema='main')
    ticker_str = "'"+"','".join(universe)+"'"
    insert_stmt = f'insert into main.universe select * from dbo.v_universe where ticker in ({ticker_str})'
    db.execute_sql(insert_stmt)

def update_portfolio(portfolio):
    db = SQLDatabase()
    db.truncate_table(table_name='im_portfolio',schema='dbo')
    for tickers in portfolio:
        ticker = "'" + tickers + "'"
        insert_stmt = f'insert into dbo.im_portfolio values ({ticker}, {portfolio[tickers]})'
        print(insert_stmt)
        db.execute_sql(insert_stmt)
    db.truncate_table(table_name='portfolio', schema='main')
    insert_stmt = f'insert into main.portfolio select * from dbo.v_portfolio'
    db.execute_sql(insert_stmt)



if __name__ == "__main__":
    #update_universe(UNIVERSE)
    update_portfolio(PORTFOLIO)