import yfinance as yf

goog = yf.Ticker('goog')
hist = goog.history(period='1mo')
print(hist)
print(goog.info)

