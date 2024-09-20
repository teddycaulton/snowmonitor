import pandas as pd 
from snowflake.snowpark.session import Session
import streamlit as st
import sys
sys.path.append('./src')
from helpers import helpers
from st_paywall import add_auth

st.set_page_config(
    page_title = "Session Creation"
)

add_auth(required=True)

with st.form("Account Login"):
    username = st.text_input('username')
    password = st.text_input('password')
    account = st.text_input('account')
    role = st.text_input('role')
    warehouse = st.text_input('warehouse')
    submitted = st.form_submit_button("Login")
    if submitted:
        try:
            st.session_state['session'] = helpers.create_snowpark_session(username, password, account, role, warehouse)
        except Exception as e:
            st.write(f"Login Failed: {e}")


