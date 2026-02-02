import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("crypto.db")
df = pd.read_sql("SELECT * FROM prices ORDER BY timestamp DESC LIMIT 1000", conn)

st.title("📈 Real-Time Crypto Dashboard")
st.line_chart(df.pivot(index="timestamp", columns="coin", values="price"))
