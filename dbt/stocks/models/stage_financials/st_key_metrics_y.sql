SELECT cast(SYMBOL as varchar2(20)) as ticker,
cast(to_date(substr("date",1,10),'yyyy-mm-dd') as date) as date_sent, 
cast(PERIOD as varchar2(20)) as period,
ROUND(cast("revenuePerShare" as number), 3) as revenue_per_share,
ROUND(cast("netIncomePerShare" as number), 3) as net_income_per_share,
ROUND(cast("operatingCashFlowPerShare" as number), 3) as operating_cash_flow_per_share,
ROUND(cast("freeCashFlowPerShare" as number), 3) as free_cash_flow_per_share,
ROUND(cast("cashPerShare" as number), 3) as cash_per_share,
ROUND(cast(POCFRATIO as number), 3) as pocf_ratio,
ROUND(cast("bookValuePerShare" as number), 3) as book_value_per_share,
ROUND(cast("tangibleBookValuePerShare" as number), 3) as tangible_book_value_per_share,
ROUND(cast("shareholdersEquityPerShare" as number), 3) as shareholders_equity_per_share,
ROUND(cast("interestDebtPerShare" as number), 3) as interest_debt_per_share,
ROUND(cast("marketCap" as number), 3) as market_cap,
ROUND(cast("enterpriseValue" as number), 3) as enterprise_value,
ROUND(cast("peRatio" as number), 3) as pe_ratio,
ROUND(cast("priceToSalesRatio" as number), 3) as price_to_sales_ratio,
ROUND(cast("pfcfRatio" as number), 3) as pfcf_ratio,
ROUND(cast("pbRatio" as number), 3) as pb_ratio,
ROUND(cast("ptbRatio" as number), 3) as ptb_ratio,
ROUND(cast("evToSales" as number), 3) as ev_to_sales,
ROUND(cast(ROIC as number), 3) as roic,
ROUND(cast("enterpriseValueOverEBITDA" as number), 3) as enterprise_value_over_ebitda,
ROUND(cast("evToOperatingCashFlow" as number), 3) as ev_to_operating_cash_flow,
ROUND(cast("earningsYield" as number), 3) as earnings_yield,
ROUND(cast("freeCashFlowYield" as number), 3) as free_cash_flow_yield,
ROUND(cast("debtToEquity" as number), 3) as debt_to_equity,
ROUND(cast("debtToAssets" as number), 3) as debt_to_assets,
ROUND(cast("netDebtToEBITDA" as number), 3) as net_debt_to_e_b_i_t_d_a,
ROUND(cast("currentRatio" as number), 3) as current_ratio,
ROUND(cast("interestCoverage" as number), 3) as interest_coverage,
ROUND(cast("incomeQuality" as number), 3) as income_quality,
ROUND(cast("dividendYield" as number), 3) as dividend_yield,
ROUND(cast("payoutRatio" as number), 3) as payout_ratio,
ROUND(cast("salesGeneralAndAdministrativeToRevenue" as number), 3) as sales_general_and_administrative_to_revenue,
ROUND(cast("researchAndDdevelopementToRevenue" as number), 3) as research_and_ddevelopement_to_revenue,
ROUND(cast("intangiblesToTotalAssets" as number), 3) as intangibles_to_total_assets,
ROUND(cast("capexToOperatingCashFlow" as number), 3) as capex_to_operating_cash_flow,
ROUND(cast("capexToRevenue" as number), 3) as capex_to_revenue,
ROUND(cast("capexToDepreciation" as number), 3) as capex_to_depreciation,
ROUND(cast("stockBasedCompensationToRevenue" as number), 3) as stock_based_compensation_to_revenue,
ROUND(cast("grahamNumber" as number), 3) as graham_number,
ROUND(cast("returnOnTangibleAssets" as number), 3) as return_on_tangible_assets,
ROUND(cast("grahamNetNet" as number), 3) as graham_net_net,
ROUND(cast("workingCapital" as number), 3) as working_capital,
ROUND(cast("tangibleAssetValue" as number), 3) as tangible_asset_value,
ROUND(cast("netCurrentAssetValue" as number), 3) as net_current_asset_value,
ROUND(cast("investedCapital" as number), 3) as invested_capital,
ROUND(cast("averageReceivables" as number), 3) as average_receivables,
ROUND(cast("averagePayables" as number), 3) as average_payables,
ROUND(cast("averageInventory" as number), 3) as average_inventory,
ROUND(cast("daysSalesOutstanding" as number), 3) as days_sales_outstanding,
ROUND(cast("daysPayablesOutstanding" as number), 3) as days_payables_outstanding,
ROUND(cast("daysOfInventoryOnHand" as number), 3) as days_of_inventory_on_hand,
ROUND(cast("receivablesTurnover" as number), 3) as receivables_turnover,
ROUND(cast("payablesTurnover" as number), 3) as payables_turnover,
ROUND(cast("inventoryTurnover" as number), 3) as inventory_turnover,
ROUND(cast(ROE as number), 3) as roe,
ROUND(cast("capexPerShare" as number), 3) as capex_per_share
FROM
    {{source('STOCK_IMPORT','IM_KEY_METRICS_BULK_ANNUAL')}} 
