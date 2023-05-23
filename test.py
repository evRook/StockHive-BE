import yfinance as yf
import json
import pandas as pd
import datetime as date
import ast



# goog = yf.Ticker('msft')
# hist = goog.history(period='1mo')
# print(type(hist))

# list = hist.values.tolist()
# print(type(list))
# print(list)
# print(hist)

# earnings = goog.shares
# print(earnings)


# print(goog.history_metadata.symbol)
# print(goog.info)

# Start = "2015-01-01"
# data = yf.download('AAPL', period='1mo')

# print(data.Close)


# pretty = goog.history_metadata
# # # print(pretty)
# print(type(pretty))
# # pretty = pretty.replace("\'", "\"")
# # pretty_eval = ast.literal_eval(pretty)
# # pretty_obj = json.loads(pretty.encode('utf-8'))
# # print(type(pretty_obj))
# print(pretty['symbol'])



# list_of_tickers = gt.get_tickers()
# df = pd.read_csv(list_of_tickers)
# print(df)


# ticker = yf.Ticker('AAPL')
# meta = ticker.history_metadata
# history = ticker.history(period='1mo')
# history_list = history.values.tolist()
# context = [{
#     'symbol': meta['symbol'],
#     'validRanges': meta['validRanges'],
#     'Open': [],
#     'Close': [],
#     'High': [],
#     'Low': [],
#     'Volume': []
# }]
# for hist in history_list:
#     context[0]['Open'].append(
#         hist[0], 
#     )
#     context[0]['Close'].append(
#         hist[1], 
#     )
#     context[0]['High'].append(
#         hist[2], 
#     )
#     context[0]['Low'].append(
#         hist[3], 
#     )
#     context[0]['Volume'].append(
#         hist[4], 
#     )
    

# print(goog.revenue_forecasts)




# def get(self, request, pk, pk_alt):
#     ticker = yf.Ticker(pk)
#     meta = ticker.history_metadata
#     history = ticker.history(period=pk_alt)
#     history_list = history.values.tolist()
#     context = [{
#         'symbol': meta['symbol'],
#         'validRanges': meta['validRanges'],
#         'Open': [],
#         'Close': [],
#         'High': [],
#         'Low': [],
#         'Volume': []
#     }]
#     for hist in history_list:
#         context[0]['Open'].append(
#             hist[0], 
#         )
#         context[0]['Close'].append(
#             hist[1], 
#         )
#         context[0]['High'].append(
#             hist[2], 
#         )
#         context[0]['Low'].append(
#             hist[3], 
#         )
#         context[0]['Volume'].append(
#             hist[4], 
#         )

#     return context

tickerArr = ['aapl', 'msft', 'tsla', 'f', 'meta', 'jnj', 'wmt', 'jpm',  'intc', 'googl', 'aapl', 'pypl', 'amzn', 'amd', 'nvda', 'gme', 'ko' ]
tick = yf.Ticker('aapl', 'msft', 'tsla')
contextArr = []
for ticker in tickerArr:
    ticker_info = tick.info
    context = [{
        'symbol': ticker_info['symbol'],
        'shortName': ticker_info['shortName'],
        'currentPrice': ticker_info['currentPrice'],
        'regularMarketPreviousClose': ticker_info['regularMarketPreviousClose'],
    }]
    contextArr.append(context)

print(contextArr)

