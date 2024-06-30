import pandas as pd 
from snowflake.snowpark.session import Session

class helpers:
    def create_snowpark_session(username, password, account, role = "ACCOUNTADMIN", warehouse = "COMPUTE_WH"):

        connection_params = {
        "user" : username,
        "password" : password,
        "account" : account,
        "role" : role,
        "warehouse" : warehouse
        }
        # create snowpark session
        session = Session.builder.configs(connection_params).create()
        return session

    def execute_sql(session, command):
        sql_command = session.sql(command)
        return sql_command.collect()
    
    def execute_sql_pandas(session, command):
        sql_command = session.sql(command)
        return sql_command.to_pandas()
    
    def querify_list(list):
        string = ""
        for i in list:
            string = string + f"{i}, "
        string = string[:-2]
        return string
    def read_current_alerts(session):
        helpers.execute_sql(session, "USE ROLE ACCOUNTADMIN")
        current_alerts = pd.DataFrame(helpers.execute_sql(session, "SHOW ALERTS"))[["name", "database_name", "schema_name", "owner", "schedule", "state", "condition", "action"]]
        # print(current_alerts)
        return current_alerts
    
    def read_alert_history(session, alert_name):
        alert_history = helpers.execute_sql_pandas(session, f"SELECT NAME, SCHEDULED_TIME, COMPLETED_TIME, ERROR_CODE, ERROR_MESSAGE, STATE FROM SNOWFLAKE.ACCOUNT_USAGE.ALERT_HISTORY WHERE NAME = '{alert_name}' ORDER BY SCHEDULED_TIME DESC")
        return alert_history