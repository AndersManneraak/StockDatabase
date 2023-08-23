select distinct 
cast(symbol as VARCHAR2(20)) as ticker, 
cast(name as VARCHAR2(500)) as company_name,
cast(price as number (17,2)) as price,
cast("changesPercentage" as number (17,2)) as changes_percentage,
cast(change as number (17,2)) as CHANGE,
cast("dayLow" as number (17,2)) as day_low,
cast("dayHigh" as number (17,2)) as day_high,
cast("yearHigh" as number (17,2)) as year_high,
cast("yearLow" as number (17,2)) as year_low,
cast("priceAvg50" as number (17,2)) as price_avg_50_days,
cast("priceAvg200" as number (17,2)) as price_avg_200_days,
cast(volume as number) volume,
cast("avgVolume" as number (17,2)) as avg_volume,
cast(open as number (17,2)) as open,
cast("previousClose" as number (17,2)) as previous_close
from {{source('STOCK_IMPORT','IM_COMMODITIES')}}