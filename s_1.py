# مراحل تحلیل داده
# 1.Data extraction  2.Data cleaning 3.Data normalization(scaling) 4.analysis 5.feature extraction 6.process with AI model  & visualization in all stages

# students = [
#     ["ali" , 12, 15]
#     ["reza"]
#     ["mohsen"]
# ]

# what we defined above is not an array and is just a python list because the numbers of columns doesnt match with each other


import pandas as pd
# pd.read_csv()
# pd.read_excel()
# pd.read_json()
#pd.read_xml()
# pd.read_clipboard()
# pd.read_html()
# data = pd.read_csv("pokemon_data.csv")
#
# data.to_excel()
# data.to_csv()

#
# import yfinance as yf
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# BTC = yf.download("BTC-USD", start="2019-07-12")
# print(BTC)
# open_price =BTC["Open"]
# print(BTC[["Open", "Close"]])
#
#
# plt.plot(open_price)
#
# # plt.legand()
# plt.show()

import streamlit as st

st.title("Data Analysis 01")

if st.button("View BTC"):

    btc = pd.read_csv("D:\programming\data_analysis_mesbah\Mesbah_Data_analysis/BTC-USD.csv")
    st.write(btc)
