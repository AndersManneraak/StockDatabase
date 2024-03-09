import streamlit as st
from sql_database import SQLDatabase  

db = SQLDatabase()
df = db.fetch_query_result("select * from stage_financials.st_balance_sheet_y where ticker = 'GME'")
reset_df = df.set_index(['calendar_year'])
trans_df = reset_df.transpose()
reversed_df = trans_df[reversed(trans_df.columns)]

with st.sidebar:
    st.dataframe(reversed_df, use_container_width=True)