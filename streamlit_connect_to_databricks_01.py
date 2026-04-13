
#install:
#python3 -m pip install streamlit databricks-sql-connector pandas
#execution: streamlit run streamlit_connect_to_databricks_01.py

import streamlit as st
import pandas as pd
import databricks.sql

#databricks auth login --host https://dbx.cloud.databricks.com
#cat ~/.databricks/token-cache.json
dbx_server_name = "dbx.cloud.databricks.com"
dbx_http_path = "/sql/1.0/warehouses/12345"
dbx_access_token = "aaa"
dbx_database = "km_db"
dbx_schema = "km_schema"


st.title("Databricks Table Row Counts")
# Sidebar: Databricks connection details
st.sidebar.header("Databricks Connection")
server_hostname = st.sidebar.text_input("Server Hostname", dbx_server_name)
http_path = st.sidebar.text_input("HTTP Path", dbx_http_path)
access_token = st.sidebar.text_input("Access Token", dbx_access_token)  #, type="password")
database = st.sidebar.text_input("Database", dbx_database)
schema = st.sidebar.text_input("Schema", dbx_schema)
show_data = st.sidebar.button("Show Row Counts")


df = pd.DataFrame()

if show_data:
    try:
        with databricks.sql.connect(
            server_hostname=server_hostname,
            http_path=http_path,
            access_token=access_token
        ) as connection:
            with connection.cursor() as cursor:
                # ---- Get all tables in the schema ----
                # cursor.execute(f"SHOW TABLES IN {schema}")
                # rows = cursor.fetchall()
                # Each row: (database, tableName, ...)
                # table_names = [row[1] for row in rows]
                cursor.execute(
                    f"SELECT table_name FROM {database}.INFORMATION_SCHEMA.tables where table_catalog='{database}' and table_schema = '{schema}'")
                rows = cursor.fetchall()
                table_names = [row[0] for row in rows]
                #table_names = [".".join([row[0], row[1], row[2]]) for row in rows]

                results = []
                for tbl in table_names:
                    full_name = f"{database}.{schema}.{tbl}"
                    try:
                        cursor.execute(f"SELECT COUNT(*) FROM {full_name}")
                        row_count = cursor.fetchone()[0]
                        results.append({'database':database, 'schema':schema, 'table': tbl, 'row_count': row_count})
                    except Exception as e:
                        results.append({'database': database, 'schema': schema, 'table': tbl, 'row_count': None})

                df = pd.DataFrame(results)
        cursor.close()
        connection.close()
    except Exception as e:
        st.error(f"Failed to connect or fetch data: {e}")

# Show the DataFrame in Streamlit
if not df.empty:
    df = df.sort_values(by="table", ascending=True)
    st.dataframe(df)
elif show_data:
    st.write("No tables found or there was an error.")

