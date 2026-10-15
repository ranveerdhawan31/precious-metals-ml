import pandas as pd
import plotly.express as px
import yfinance as yf


# Download approximately one month of gold futures data.
gold_data = yf.download(
    "GC=F",
    period="1mo",
    auto_adjust=False,
    progress=False,
)

# Download approximately one month of silver futures data.
silver_data = yf.download(
    "SI=F",
    period="1mo",
    auto_adjust=False,
    progress=False,
)


# Display information about the downloaded data.
print("Data source: Yahoo Finance through yfinance")
print("Instruments: Gold futures and silver futures")
print("Tickers: GC=F and SI=F")
print("Currency: USD")
print("Requested period: 1 month")
print()


# Inspect the raw gold data.
print("Gold data:")
print(gold_data.head())
print("\nGold table shape:", gold_data.shape)


# Inspect the raw silver data.
print("\nSilver data:")
print(silver_data.head())
print("\nSilver table shape:", silver_data.shape)


# Check whether both datasets contain the same dates.
dates_match = gold_data.index.equals(silver_data.index)

print("\nDo gold and silver dates match?", dates_match)


# Extract the closing-price columns.
gold_close = gold_data["Close"].squeeze()
silver_close = silver_data["Close"].squeeze()

print("\nGold closing prices:")
print(gold_close.head())

print("\nSilver closing prices:")
print(silver_close.head())


# Combine gold and silver closing prices into one table.
combined_data = pd.DataFrame(
    {
        "Gold_Close": gold_close,
        "Silver_Close": silver_close,
    }
)

print("\nCombined gold and silver data:")
print(combined_data.head())

print("\nCombined table shape:", combined_data.shape)


# Check for missing prices.
print("\nMissing values in each column:")
print(combined_data.isna().sum())


# Check whether any trading date appears more than once.
duplicate_dates = combined_data.index.duplicated().sum()

print("\nNumber of duplicate dates:", duplicate_dates)


# Check whether any price is zero or negative.
non_positive_prices = (combined_data <= 0).sum()

print("\nNon-positive prices in each column:")
print(non_positive_prices)


# Calculate daily decimal returns.
combined_data["Gold_Return"] = combined_data["Gold_Close"].pct_change()
combined_data["Silver_Return"] = combined_data["Silver_Close"].pct_change()

print("\nData with daily returns:")
print(combined_data.head())


# Convert decimal returns into percentages for easier reading.
combined_data["Gold_Return_Percent"] = (
    combined_data["Gold_Return"] * 100
)

combined_data["Silver_Return_Percent"] = (
    combined_data["Silver_Return"] * 100
)

print("\nDaily returns displayed as percentages:")
print(
    combined_data[
        ["Gold_Return_Percent", "Silver_Return_Percent"]
    ]
    .head()
    .round(2)
)


# Calculate the gold-silver ratio.
combined_data["Gold_Silver_Ratio"] = (
    combined_data["Gold_Close"] / combined_data["Silver_Close"]
)

print("\nGold-silver ratio:")
print(
    combined_data["Gold_Silver_Ratio"]
    .head()
    .round(2)
)


# Normalize both metals so each one starts at 100.
combined_data["Gold_Normalized"] = (
    combined_data["Gold_Close"]
    / combined_data["Gold_Close"].iloc[0]
) * 100

combined_data["Silver_Normalized"] = (
    combined_data["Silver_Close"]
    / combined_data["Silver_Close"].iloc[0]
) * 100


# Create the normalized relative-performance graph.
price_figure = px.line(
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


# Open the interactive graph in the browser.
price_figure.show()