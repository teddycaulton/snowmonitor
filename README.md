# Snowmonitor: a UI driven approach to alert management in Snowflake

Alert creation and management in Snowflake can be a hassle, particularly at scale.  All creation and monitoring of alerts occurs within SQL so monitoring alert executions and failures means querying the information schema with various different name and date filters.  For 5-10 alerts this is management even for novice Snowflake users but once a portfolio of alerts expands it can be a hassle to monitor.  I recently worked on a project where I was prototying ~20 alerts and the process of standing them up, executing unit tests and then tracking success or failure was difficult to manage.  Snowmonitor attempts to streamline this process, offering a scalable streamlit app that can track alerts across an entire Snowflake account, included as features:
- monitor alerts across an entire Snowflake account
- Suspend, resume, execute and delete alerts at the click of a button
- Create new alerts using an easy to operate wizard, no more looking up documentation to check required and optional parameters

## Prerequisites

Make sure you have the following installed:
- Python 3.10+
- `pip` or `conda` (Python package manager)
- Standard edition or higher version of Snowflake

## Installation

1. Clone the repository:

2. Create a virtual environment and activate it:
    ```bash
    conda create -n snowmonitor python=3.10
    conda activate snowmonitor
    ```
3. Install the required packages:

4. Create a `.env` file in the root directory of the project and add your configuration variables:
    ```plaintext
    username=
    password=
    account=
    role=
    warehouse=
    ```

## Usage

- Launch the streamlit app in a local environment:
    ```bash
    streamlit run 0_Alert_Management.py
    ```

- Host your streamlit app in the cloud:
    I would reccomend either running the app locally if you're the only admin or hosting it on a private streamlit app for multiple administrators.  In the latter case, replace the environment variables with st.secrets() and add the secrets in streamlit cloud.  I will be releasing a version for native apps shortly.
