import streamlit as st
import pandas as pd

CSV_URL = "https://raw.githubusercontent.com/nitsingh89/ongc_dcs_dashboard/main/dcs_log_temp.csv"

st.set_page_config(page_title="ONGC DCS Flow", layout="centered")

st.title("ONGC – Live DCS Flow Dashboard")

@st.cache_data(ttl=5)
def load_data():
    df = pd.read_csv(CSV_URL)

    # DEBUG
    st.write("Rows:", len(df))
    st.write(df.tail())

    return df

try:
    df = load_data()

    if len(df) == 0:
        st.error("CSV loaded but empty")
    else:
        latest = df.iloc[-1]

        st.metric("Flow", latest["Flow"])
        st.caption(f"Last Update: {latest['Time']}")

        st.line_chart(df["Flow"])

except Exception as e:
    st.error("Streamlit error")
    st.write(e)
