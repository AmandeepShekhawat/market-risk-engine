import yfinance as yf
import pandas as pd

SYMBOLS = [
    # Energy ETFs
    "XLE",     # Energy Select Sector ETF
    "VDE",     # Vanguard Energy ETF

    # Oil & Gas Majors
    "XOM",     # Exxon Mobil
    "CVX",     # Chevron

    # US Shale / E&P
    "EOG",     # EOG Resources

    # Oilfield Services
    "SLB",     # Schlumberger
    "HAL",     # Halliburton
]

def fetch_prices():
    
    data = yf.download(SYMBOLS, start="2018-01-01")
    data = data.stack(1).reset_index()
    data = data.rename(columns={"Ticker":"symbol"})

    return data

def transform_prices(df):

    df.columns = [col[0] if isinstance(col,tuple) else col for col in df.columns]
    df = df.rename(columns = {
        "Date" : "date",
        "Open" : "open",
        "High" : "high",
        "Low" : "low",
        "Close":"close",
        "Volume" : "volume"
    })
    
    df = df [["symbol","date","open","high","low","close","volume"]]

    return df