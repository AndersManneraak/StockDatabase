import streamlit as st
from sql_database import SQLDatabase  

db = SQLDatabase()
df = db.fetch_query_result("select * from stage_financials.st_balance_sheet_y where ticker = 'GME'")
reset_df = df.set_index(['calendar_year'])
sorted_df = reset_df.sort_index(axis=0, ascending=False, inplace=False, kind="quicksort")
trans_df = sorted_df.transpose()
reversed_df = trans_df[reversed(trans_df.columns)]
print(reversed_df)

with st.sidebar:
    st.dataframe(reversed_df, use_container_width=True)