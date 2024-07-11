import pandas as pd 
from snowflake.snowpark.session import Session
import streamlit as st
import sys
sys.path.append('./src')
from helpers import helpers

st.set_page_config(
    page_title = "Alert Creation"
)

session = helpers.create_snowpark_session('tcaulton', 'Foo1234!', 'QTB38119', 'accountadmin', 'compute_wh')

st.title(":blue[Alert Creation] 🔔")
st.header("Create alerts using the wizard below", divider='rainbow')

role = st.text_input("What role do you want to use (case sensitive and host user must have access to it)")
replace_or_new = st.selectbox("Are you replacing or creating from scratch", ("Replacing", "Creating from Scratch"))
name = st.text_input("Alert Name (Fully Qualify With Database and Schema)")
schedule = st.text_input("Schedule")
comment = st.text_input("Comment (Optional)")
# tag = st.text_input("Tag")
condition = st.text_input("Condition")
action = st.text_input("Action")
warehouse = st.text_input("Warehouse (Optional)")

# Define optional field values for query creation
if len(warehouse) > 0:
    warehouse_query = f"WAREHOUSE = {warehouse}"
else:
    warehouse_query = ''

if len(comment) > 0:
    comment_query = f"COMMENT = '{comment}'"
else:
    comment_query = ''

# Define Creation Query
if replace_or_new == "Replacing":
    alert_generation_query = f'''CREATE OR REPLACE ALERT {name}
                                {warehouse_query}
                                SCHEDULE = '{schedule}'
                                {comment_query}
                                IF( EXISTS(
                                {condition}
                                ))
                                THEN
                                {action}'''
else:
    alert_generation_query = f'''CREATE ALERT IF NOT EXISTS {name}
                                {warehouse_query}
                                SCHEDULE = '{schedule}'
                                {comment_query}
                                IF( EXISTS(
                                {condition}
                                ))
                                THEN
                                {action}'''

# st.write(alert_generation_query)
auto_resume = st.checkbox("Auto-Start This Alert")
if st.button("Create Alert"):
    try:
        helpers.execute_sql(session, f"USE ROLE {role}")
        helpers.execute_sql(session, alert_generation_query)
        if auto_resume:
            st.write("resuming")
            helpers.execute_sql(session, f'ALTER ALERT {name} RESUME')
        st.write("Alert Successfully Created")
    except Exception as e:
        st.error(f"The Alert Wizard Resulted in an error: '{e}'")



