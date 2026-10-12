import yfinance as yf

gold_data = yf.download(
    "GC=F",
    period="1mo",
    auto_adjust=False,
    progress=False,
)

print(gold_data.head())

print("\nTable shape:", gold_data.shape)