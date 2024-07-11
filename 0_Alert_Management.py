import pandas as pd 
from snowflake.snowpark.session import Session
import streamlit as st
import sys
sys.path.append('./src')
from helpers import helpers

st.set_page_config(
    page_title = "Alert Management"
)

session = helpers.create_snowpark_session('tcaulton', 'Foo1234!', 'QTB38119', 'accountadmin', 'compute_wh')

st.title(":blue[SnowMonitor] 🔎")
st.header("UI Driven Snowflake Alert Management")

st.subheader('Current Alerts', divider='rainbow')
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
        st.error("Be sure you want to select the buttons below")
        button1, button2, button3 = st.columns(3)
        with button1:
            if st.button("Delete Alert", key = f'{row[0]}_delete_alert'):
                helpers.execute_sql(session, f"DROP ALERT IF EXISTS {row[1]}.{row[2]}.{row[0]}")
        with button2:
            if row[5] == 'suspended':
                if st.button("Resume Alert", key = f'{row[0]}_resume_alert'):
                    helpers.execute_sql(session, f"ALTER ALERT {row[1]}.{row[2]}.{row[0]} RESUME")
                    st.rerun()
            elif row[5] == 'started':
                if st.button("Suspend Alert", key = f'{row[0]}_suspend_alert'):
                    helpers.execute_sql(session, f"ALTER ALERT {row[1]}.{row[2]}.{row[0]} SUSPEND")
                    st.rerun()
        with button3:
            if row[5] == 'started':
                if st.button("Execute Alert", key = f'{row[0]}_execute_alert'):
                    helpers.execute_sql(session, f"EXECUTE ALERT {row[1]}.{row[2]}.{row[0]}")
