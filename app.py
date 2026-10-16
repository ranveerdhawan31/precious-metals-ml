import pandas as pd
import plotly.express as px
import streamlit as st
import yfinance as yf


st.set_page_config(
    page_title="Precious Metals ML",
    page_icon="📊",
    layout="wide",
)

gold_data = yf.download(
    "GC=F",
    period="1mo",
    auto_adjust=False,
    progress=False,
)

silver_data = yf.download(
    "SI=F",
    period="1mo",
    auto_adjust=False,
    progress=False,
)

gold_close = gold_data["Close"].squeeze()
silver_close = silver_data["Close"].squeeze()

combined_data = pd.DataFrame(
    {
        "Gold_Close": gold_close,
        "Silver_Close": silver_close,
    }
)

combined_data["Gold_Normalized"] = (
    combined_data["Gold_Close"]
    / combined_data["Gold_Close"].iloc[0]
) * 100

combined_data["Silver_Normalized"] = (
    combined_data["Silver_Close"]
    / combined_data["Silver_Close"].iloc[0]
) * 100

performance_figure = px.line(
    combined_data,
    x=combined_data.index,
    y=["Gold_Normalized", "Silver_Normalized"],
    title="Gold and Silver Relative Performance",
    labels={
        "value": "Performance Index (Starting Value = 100)",
        "Date": "Trading Date",
        "variable": "Metal",
    },
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

st.plotly_chart(
    performance_figure,
    width="stretch",
)
