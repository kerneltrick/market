import yfinance as yf

def get_historical_prices(symbol = 'NVDA', startDate = '2020-11-01', endDate = '2020-12-01', granularity = '1d'):
    """
    Retrieve high, low, close, open, volume, dividends, splits 
    over specified time period.

    Inputs
    ------
    symbol (str) - NYSE ticker acronym
    startDate (str) - first day in range, yyyy-mm-dd
    endDate (str) - last day in range, yyyy-mm-dd
    granularity (str) - sampling frequency {1d,1m,1y}
    """
    stock = yf.Ticker(symbol)
    priceHistory = stock.history(interval = granularity, start = startDate, end = endDate)
    priceHistory.to_csv('/home/mark/docs/projects/market/data/historical_prices.csv')
    return priceHistory
