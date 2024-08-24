import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import datetime
# data = yf.download("BTC-USD")
# df = pd.DataFrame(data)
# df.to_csv("BTC.CSV")

data = pd.read_csv("BTC.CSV")
df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])
df["week_day"] = df["Date"].apply(lambda x: x.weekday())

df = df.drop(columns=["Low", "Volume", "Adj Close"])

# 2 is wednesday and 5 is saturday
selected_days = [2 , 5]
df = df[df['week_day'].isin(selected_days)]

start_date = '2019-01-01'
end_date = '2024-05-08'

df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
df = df.drop(df.index[0])


df["week_close"] = df["Close"].shift(-1)
df["week_high"] = df["High"].shift(-1)

df["close_week_profit"] = df["week_close"] / df["Open"]
df["high_week_profit"] = df["week_high"] / df["Open"]


df.reset_index(drop=True, inplace=True)



starting_dollars_if_close = 1000
starting_dollars_if_high = 1000


start_of_week_dollars_if_close = []
end_of_week_dollars_if_close = []
start_of_week_dollars_if_high = []
end_of_week_dollars_if_high = []


for i in range(len(df)):
    start_of_week_dollars_if_close.append(starting_dollars_if_close)
    end_of_week_dollars_value = starting_dollars_if_close * df.loc[i, 'close_week_profit']
    end_of_week_dollars_if_close.append(end_of_week_dollars_value)
    starting_dollars_if_close = end_of_week_dollars_value

for i in range(len(df)):
    start_of_week_dollars_if_high.append(starting_dollars_if_high)
    end_of_week_dollars_value = starting_dollars_if_high * df.loc[i, 'high_week_profit']
    end_of_week_dollars_if_high.append(end_of_week_dollars_value)
    starting_dollars_if_high = end_of_week_dollars_value




# Add the results to the DataFrame
df['Start_of_Week_Dollars_if_close'] = start_of_week_dollars_if_close
df['End_of_Week_Dollars_if_close'] = end_of_week_dollars_if_close

df['Start_of_Week_Dollars_if_high'] = start_of_week_dollars_if_high
df['End_of_Week_Dollars_if_high'] = end_of_week_dollars_if_high



df.to_csv("Analysed_BTC.csv")

plt.plot(df["Start_of_Week_Dollars_if_close"][:200], label="Close", color="green")
plt.plot(df["Start_of_Week_Dollars_if_high"][:200], label="High", color="red")
plt.legend()
plt.show()


plt.plot(df["Start_of_Week_Dollars_if_close"], label = "Close", color = "green")
plt.plot(df["Start_of_Week_Dollars_if_high"], label= "High" , color = "red")
plt.legend()
plt.show()


plt.subplot(2,2,1)
plt.plot(df["Start_of_Week_Dollars_if_close"], label = "Close", color = "green")

plt.subplot(2,2,2)
plt.plot(df["Start_of_Week_Dollars_if_high"], label= "High" , color = "red")

plt.subplot(2,1,2)
plt.plot(df["close_week_profit"], label= "close", color = "green")
plt.plot(df["high_week_profit"], label= "High" , color = "red")



plt.legend()
plt.show()

df.info()
print(df)