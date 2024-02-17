import re

def reformat_sql_select_list(input_sql_list):
    # Regular expression to match the pattern: cast(columnName as type) as ColumnName
    pattern = re.compile(r'cast\((.*?) as (.*?)\) as (\w+)', re.IGNORECASE)

    # Find all matches in the input string
    matches = pattern.findall(input_sql_list.replace('\n', ' '))

    reformatted_statements = []

    for match in matches:
        column_name, column_type, alias = match

        # Function to convert CamelCase alias to snake_case
        def camel_to_snake(name):
            return ''.join(['_'+c.lower() if c.isupper() else c for c in name]).lstrip('_')

        # Converting only the alias to snake_case
        alias_snake_case = camel_to_snake(alias)

        # Assembling the reformatted SQL statement
        reformatted_sql = f'cast("{column_name}" as {column_type}) as {alias_snake_case}'
        reformatted_statements.append(reformatted_sql)

    # Combining the reformatted statements back into a comma-separated list
    reformatted_sql_list = ", ".join(reformatted_statements)

    return reformatted_sql_list

# Example usage with a multiline string input
input_sql_list = """cast(calendarYear as varchar(100)) as CalendarYear, 
cast(PERIOD as number) as Period, 
cast(netIncome as number) as NetIncome, 
cast(depreciationAndAmortization as number) as DepreciationAndAmortization, 
cast(deferredIncomeTax as number) as DeferredIncomeTax, 
cast(stockBasedCompensation as number) as StockBasedCompensation, 
cast(changeInWorkingCapital as number) as ChangeInWorkingCapital, 
cast(accountsReceivables as number) as AccountsReceivables, 
cast(INVENTORY as number) as Inventory, 
cast(accountsPayables as number) as AccountsPayables, 
cast(otherWorkingCapital as number) as OtherWorkingCapital, 
cast(otherNonCashItems as varchar(100)) as OtherNonCashItems, 
cast(netCashProvidedByOperatingActivites as number) as NetCashProvidedByOperatingActivities, 
cast(investmentsInPropertyPlantAndEquipment as number) as InvestmentsInPropertyPlantAndEquipment, 
cast(acquisitionsNet as number) as AcquisitionsNet, 
cast(purchasesOfInvestments as number) as PurchasesOfInvestments, 
cast(salesMaturitiesOfInvestments as number) as SalesMaturitiesOfInvestments, 
cast(otherInvestingActivites as varchar(100)) as OtherInvestingActivities, 
cast(netCashUsedForInvestingActivites as number) as NetCashUsedForInvestingActivities, 
cast(debtRepayment as number) as DebtRepayment, 
cast(commonStockIssued as varchar(100)) as CommonStockIssued, 
cast(commonStockRepurchased as varchar(100)) as CommonStockRepurchased, 
cast(dividendsPaid as number) as DividendsPaid, 
cast(otherFinancingActivites as varchar(100)) as OtherFinancingActivities, 
cast(netCashUsedProvidedByFinancingActivities as number) as NetCashUsedProvidedByFinancingActivities,
cast(effectOfForexChangesOnCash as varchar(100)) as EffectOfForexChangesOnCash, 
cast(netChangeInCash as number) as NetChangeInCash, 
cast(cashAtEndOfPeriod as number) as CashAtEndOfPeriod, 
cast(cashAtBeginningOfPeriod as number) as CashAtBeginningOfPeriod, 
cast(operatingCashFlow as number) as OperatingCashFlow, 
cast(capitalExpenditure as number) as CapitalExpenditure, 
cast(freeCashFlow as number) as FreeCashFlow"""

reformatted_sql_list = reformat_sql_select_list(input_sql_list)
print(reformatted_sql_list)
