import streamlit as st

st.set_page_config(
    page_title="Precious Metals ML",
    page_icon="📊",
    layout="wide",
)

st.title("Precious Metals Market Analyzer")

st.write(
    "Explore historical gold and silver market behaviour using "
    "Python, data analysis, and machine learning."
)

st.info(
    "This project analyzes historical market data for educational purposes. "
    "It does not provide financial advice or guaranteed predictions."
)