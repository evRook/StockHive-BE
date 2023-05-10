import yfinance as yf
import json
import pandas as pd
import datetime as date



goog = yf.Ticker('AAPL')
hist = goog.history(period='1mo')

# print(goog.history_metadata.symbol)
# print(goog.info)

# Start = "2015-01-01"
# data = yf.download('AAPL', period='1mo')

# print(data.Close)


# pretty = str(goog.history_metadata)
# # print(pretty)
# pretty_obj = json.loads(pretty)
# print(pretty_obj)
pretty_format = json.dumps(goog.info, indent=2)

print(pretty_format)

# list_of_tickers = gt.get_tickers()
# df = pd.read_csv(list_of_tickers)
# print(df)

