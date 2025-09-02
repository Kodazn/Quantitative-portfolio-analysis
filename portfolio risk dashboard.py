import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np


# Just add a manual refresh button instead
if st.button("🔄 Refresh Data"):
    st.rerun()

#Display list of Tickers
list = ["AAPL", "GOOG", "MSFT",]
Ticker = list
st.write (Ticker)

#Line chart of historical data for Apple
data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
st.write(data.head())
st.write("Historical data chart for Apple:")
st.line_chart(data['Close'])

#Line chart of historical data for Google
st.write("Historical data chart for google:")
data = yf.download("GOOG", start="2020-01-01", end="2021-01-01")
st.write(data.head())
st.write("Historical data chart for Google:")
st.line_chart(data['Close'])

#Line chart of historical data for Microsoft
st.write("Historical data chart for Microsoft:")
data = yf.download("MSFT", start="2020-01-01", end="2021-01-01")
st.write(data.head())
st.write("Historical data chart for Microsoft:")
st.line_chart(data['Close'])


#Line chart using historical data for ALL the Tickers
data = yf.download(list, start="2020-01-01", end="2021-01-01")
st.write(data.head())

st.line_chart(data['Close'])

#Calculate the daily returns for Apple
aapl_prices = data['Close']['AAPL']
aapl_returns = aapl_prices.pct_change()
st.write("AAPL Daily Returns:")
st.write(aapl_returns)

average_return = aapl_returns.mean()
st.write("AAPL Daily Average Returns:")
st.write(average_return)

#Calculate the standard deviation for Apple
standard_deviation = aapl_returns.std()
st.write("AAPL Standard Deviation")
st.write(standard_deviation)


#Calculate the daily returns for Google
GOOG_prices = data['Close']['GOOG']
GOOG_returns = GOOG_prices.pct_change()
st.write("GOOG Daily Returns:")
st.write(GOOG_returns)


average_return = GOOG_returns.mean()
st.write("GOOG Daily Average Returns")
st.write(average_return)

#Calculate the standard deviation for Google
st.write("GOOG Standard Deviation:")
standard_deviation = GOOG_returns.std()
st.write(standard_deviation)

#Calculate the daily returns for Microsoft
MSFT_prices = data['Close']['MSFT']
MSFT_returns = MSFT_prices.pct_change()
st.write("MSFT Daily Returns:")
st.write(MSFT_returns)

average_return = MSFT_returns.mean()
st.write("MSFT Daily Average Returns")
st.write(average_return)

#Calculate the standard deviation for Microsoft
st.write("MSFT Standard Deviation:")
standard_deviation = MSFT_returns.std()
st.write(standard_deviation)

sharpe_ratio = average_return / standard_deviation

#Sharpe ratio for Apple
apple_sharpe = aapl_returns.mean()/aapl_returns.std()
st.write("Apple Sharpe Ratio:", apple_sharpe)


#Sharpe ratio for Google
google_sharpe = GOOG_returns.mean()/GOOG_returns.std()
st.write("Google Sharpe Ratio:", google_sharpe)


#Sharpe ratio for Microsoft
microsoft_sharpe = MSFT_returns.mean()/MSFT_returns.std()
st.write("Microsoft Sharpe Ratio:", microsoft_sharpe)


st.write("Are they equal?", google_sharpe == microsoft_sharpe)