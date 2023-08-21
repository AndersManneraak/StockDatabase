import oracledb

connection = oracledb.connect(
    user="stock_import",
    password='Warlordmanrock95',
    dsn="localhost/orcl")

cursor = connection.cursor()

cursor.execute("select * from stock_import.my_first_dbt_model")

connection.commit()
