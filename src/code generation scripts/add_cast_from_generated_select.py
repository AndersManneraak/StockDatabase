def convert_columns_to_sql(camel_case_columns):
    # Split the input string by commas to get individual column names
    columns = camel_case_columns.split(',')
    sql_statements = []

    # Function to convert camelCase to snake_case
    def camel_to_snake(name):
        return ''.join(['_'+c.lower() if c.isupper() else c for c in name]).lstrip('_')

    # Iterate through each column, strip extra spaces and quotes, then format it
    for column in columns:
        column_cleaned = column.strip().strip('"')
        sql_statement = f'cast("{column_cleaned}" as number) as {camel_to_snake(column_cleaned)}'
        sql_statements.append(sql_statement)

    # Join the individual SQL statements with a comma and newline for the final output
    return ',\n   '.join(sql_statements)

# Example usage
input_columns = '''
    "date",
    "revenuePerShare",
    "netIncomePerShare",
    "operatingCashFlowPerShare",
    "freeCashFlowPerShare",
    "cashPerShare",
    "bookValuePerShare",
    "tangibleBookValuePerShare",
    "shareholdersEquityPerShare",
    "interestDebtPerShare",
    "marketCap",
    "enterpriseValue",
    "peRatio",
    "priceToSalesRatio",
    "pfcfRatio",
    "pbRatio",
    "ptbRatio",
    "evToSales",
    "enterpriseValueOverEBITDA",
    "evToOperatingCashFlow",
    "earningsYield",
    "freeCashFlowYield",
    "debtToEquity",
    "debtToAssets",
    "netDebtToEBITDA",
    "currentRatio",
    "interestCoverage",
    "incomeQuality",
    "dividendYield",
    "payoutRatio",
    "salesGeneralAndAdministrativeToRevenue",
    "researchAndDdevelopementToRevenue",
    "intangiblesToTotalAssets",
    "capexToOperatingCashFlow",
    "capexToRevenue",
    "capexToDepreciation",
    "stockBasedCompensationToRevenue",
    "grahamNumber",
    "returnOnTangibleAssets",
    "grahamNetNet",
    "workingCapital",
    "tangibleAssetValue",
    "netCurrentAssetValue",
    "investedCapital",
    "averageReceivables",
    "averagePayables",
    "averageInventory",
    "daysSalesOutstanding",
    "daysPayablesOutstanding",
    "daysOfInventoryOnHand",
    "receivablesTurnover",
    "payablesTurnover",
    "inventoryTurnover",
    "capexPerShare"'''

output_sql = convert_columns_to_sql(input_columns)
print(output_sql)