# app.py
import streamlit as st
import requests
import time

st.title("🚀 Real-Time Crypto Dashboard")

COINS = ["bitcoin", "ethereum", "solana"]

def get_prices():
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(COINS), "vs_currencies": "usd"}
    return requests.get(url, params=params).json()

# Live loop
placeholder = st.empty()

while True:
    data = get_prices()
    with placeholder.container():
        for coin in COINS:
            st.metric(coin.upper(), f"${data[coin]['usd']}")
    time.sleep(5)  # refresh every 5 seconds
