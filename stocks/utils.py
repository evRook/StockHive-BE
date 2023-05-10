import yfinance as yf

def load_data(ticker): 
    data = yf.download(ticker, period='1mo')
    data.reset_index(inplace=True)
    return data

def req_data(search):
    load_data(search)