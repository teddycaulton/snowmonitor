import pandas as pd 
from snowflake.snowpark.session import Session
import streamlit as st
import sys
sys.path.append('./src')
from helpers import helpers

session = helpers.create_snowpark_session('tcaulton', 'Foo1234!', 'QTB38119', 'accountadmin', 'compute_wh')

st.title("Snowmonitor: Snowflake Alert Management")

st.header("Current Alerts")
alert_data = helpers.read_current_alerts(session)
print(alert_data)
for row in alert_data.values:
    with st.expander(row[0]):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Alert Name: {row[0]}")
            st.write(f"Condition: {row[6]}")
            st.write(f"Action: {row[7]}")
            st.write(f"Owner: {row[3]}")
        with col2:
            st.write(f"Database: {row[1]}")
            st.write(f"Schema: {row[2]}")
            st.write(f"Schedule: {row[4]}")
            st.write(f"State: {row[5]}")
        if st.checkbox("Run History (last 10 runs)", key = row[0]):
            alert_history_df = helpers.read_alert_history(session, row[0])
            st.table(alert_history_df)

