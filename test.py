import yfinance as yf
import json
import pandas as pd



goog = yf.Ticker('AAPL')
hist = goog.history(period='1mo')
print(hist)
print(hist.Open)


# pretty = str(hist)
# pretty_obj = json.loads(pretty)
# pretty_format = json.dumps(pretty_obj, indent=2)

# print(pretty_format)

# list_of_tickers = gt.get_tickers()
# df = pd.read_csv(list_of_tickers)
# print(df)

