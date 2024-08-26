import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt

df = yf.download("BTC-USD")

df["Date"] = pd.to_datetime(df.index)

df["Month"] = df["Date"].dt.



