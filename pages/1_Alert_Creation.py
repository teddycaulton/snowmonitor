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

st.title("Alert Creation")

role = st.text_input("What role do you want to use (case sensitive and host user must have access to it)")
replace_or_new = st.selectbox("Are you replacing or creating from scratch", ("Replacing", "Creating from Scratch"))
name = st.text_input("Alert Name")
schedule = st.text_input("Schedule")
comment = st.text_input("Comment")
tag = st.text_input("Tag")
condition = st.text_input("Condition")
then = st.text_input("Action")
warehouse = st.text_input("Warehouse (Optional)")

if st.button("Create Alert"):
    try:
        helpers.execute_sql(session, f"USE ROLE {role}")
    except Exception as e:
        st.error("")



