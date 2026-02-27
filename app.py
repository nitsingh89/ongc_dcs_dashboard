import streamlit as st
import pandas as pd
import time

CSV_URL = "https://raw.githubusercontent.com/nitsingh89/ongc_dcs_dashboard/main/dcs_log_temp.csv"

st.set_page_config(page_title="ONGC DCS Flow", layout="centered")
st.title("ONGC – Live DCS Flow Dashboard")

def load_data():
    url = f"{CSV_URL}?t={int(time.time())}"   # bypass GitHub cache
    return pd.read_csv(url)

try:
    df = load_data()

    df = df.dropna()              # remove blank rows
    df["Flow"] = pd.to_numeric(df["Flow"], errors="coerce")

    st.write(f"Rows: {len(df)}")

    latest = df.iloc[-1]

    st.metric("Flow", f"{latest['Flow']:.3f}")
    st.caption(f"Last Update: {latest['Time']}")

    st.line_chart(df["Flow"])

except Exception as e:
    st.error("No data available")

# auto refresh every 10 sec
time.sleep(10)
st.rerun()
