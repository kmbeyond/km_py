
import streamlit as st
import pandas as pd

st.write(""" My first app""")

df_sales = pd.read_csv("/Users/km/km/km_practice/data/sample_data_graph.csv")
""" --sample data
sales_date,sales_count
2025-01-01,11
"""

st.header("Sales Chart")
st.bar_chart(df_sales, x="sales_date", y="sales_count", color=['#33C4FF'])

#st.line_chart(df_sales, x="sales_date", y="sales_count", color=['#33C4FF'])
