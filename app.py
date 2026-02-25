import streamlit as st
import pandas as pd

CSV_URL = "https://raw.githubusercontent.com/nitsingh89/ongc_dcs_dashboard/main/dcs_log.csv"

st.set_page_config(page_title="ONGC DCS Flow", layout="centered")

st.title("ONGC – Live DCS Flow Dashboard")

@st.cache_data(ttl=5)
def load_data():
    return pd.read_csv(CSV_URL)

try:
    df = load_data()

    if df.empty:
        st.error("No data available")
    else:
        df["Time"] = pd.to_datetime(df["Time"])
        latest = df.iloc[-1]

        st.metric("Flow", latest["Flow"])
        st.caption(f"Last Update: {latest['Time']}")

        st.line_chart(df.set_index("Time")["Flow"])

except Exception as e:
    st.error("No data available")
