import streamlit as st
import pandas as pd

CSV_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/dcs_log.csv"

st.set_page_config(page_title="ONGC DCS Flow", layout="centered")

st.title("ONGC – Live DCS Flow Dashboard")

@st.cache_data(ttl=5)
def load_data():
    return pd.read_csv(CSV_URL)

try:
    df = load_data()

    latest = df.iloc[-1]

    st.metric("Flow", latest["Flow"])
    st.caption(f"Last Update: {latest['Time']}")

    st.line_chart(df["Flow"])

except:
    st.error("No data available")
