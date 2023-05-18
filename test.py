import yfinance as yf
import json
import pandas as pd
import datetime as date
import ast



goog = yf.Ticker('AAPL')
hist = goog.history(period='1mo')
# print(type(hist))

list = hist.values.tolist()
print(type(list))
print(list[1])
print(list[0])

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


ticker = yf.Ticker('AAPL')
meta = ticker.history_metadata
history = ticker.history(period='1mo')
history_list = history.values.tolist()
context = []
context.append({
    'symbol': meta['symbol'],
    'validRanges': meta['validRanges']
})
for hist in history_list:
    context.append({   
        'Open': hist[0], 
        'Close': hist[1], 
        'High': hist[2],
        'Low': hist[3],
        'Volume': hist[4],
    })

print(context)

