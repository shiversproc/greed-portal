"""
analyzer.py - Core Analysis Logic
===================================
This is the brain of the app. It ties together fetching and indicators,
then produces a clean summary dict that both the CLI and web UI can consume.

Keeping this separate means we don't repeat the same logic in main.py and app.py.
That principle is called "separation of concerns" -- GOOGLE that term, it's worth knowing.
"""

from fetch import get_current_price, get_info, get_price_history
from indicators import add_all_indicators


def generate_signal(rsi, sma20, sma50):
    # TODO: if rsi < 30, return an oversold message

    # TODO: elif rsi > 70, return an overbought message
    # TODO: else return "NEUTRAL"
    if rsi < 30:
        return "OVERSOLD - possible buy zone"
    elif rsi > 70:
        return "OVERBOUGHT - possible sell zone"
    else:
        return "NEUTRAL"


def analyze(symbol, period="6mo"):

    # Pulls in company info based on ticker symbol input.
    info = get_info(symbol)
    df = get_price_history(symbol, period=period)
    df = add_all_indicators(df)

    # TODO: get the last row of df (call it 'latest')
    latest = df.iloc[-1]
    # TODO: get the RSI value from latest -- round it to 2 decimal places
    #       HINT: round(float(latest.get("RSI", 0)), 2)
    rsi = round(float(latest.get("RSI", 0)), 2)
    # TODO: get sma20 from latest -- same pattern as rsi above (key is "SMA_20")
    sma20 = round(float(latest.get("SMA_20", 0)), 2)
    # TODO: get sma50 from latest (key is "SMA_50")
    sma50 = round(float(latest.get("SMA_50", 0)), 2)
    # TODO: call generate_signal(rsi, sma20, sma50) to get the signal string
    generate_signal(rsi, sma20, sma50)
    # TODO: return a dict with all relevent fields.
    analyzed = {
        "Symbol": info.get("symbol"),
        "Name": info.get("longName"),
        "Sector": info.get("sector"),
        "Industry": info.get("industry"),
        "Country": info.get("country"),
        "Exchange": info.get("exchange"),
        "Currency": info.get("currency"),
        "Website": info.get("website"),
        "Price": info.get("currentPrice"),
        "Regular Market Price": info.get("regularMarketPrice"),
        "Previous Close": info.get("previousClose"),
        "Open": info.get("open"),
        "Daily High": info.get("dayHigh"),
        "Daily Low": info.get("dayLow"),
        "Yearly High": info.get("fiftyTwoWeekHigh"),
        "Yearly Low": info.get("fiftyTwoWeekLow"),
        "Fifty Day Avg": info.get("fiftyDayAverage"),
        "200 Day Avg": info.get("twoHundredDayAverage"),
        "Market Cap": info.get("marketCap"),
        "Trailing PE": info.get("trailingPE"),
        "Forward PE": info.get("forwardPE"),
        "Price to Book": info.get("priceToBook"),
        "PTS Trailing 12months": info.get("priceToSalesTrailing12Months"),
        "Enterprise Value": info.get("enterpriseValue"),
        "Enterprise to Revenue": info.get("enterpriseToRevenue"),
        "Enterprise to EBITA": info.get("enterpriseToEbitda"),
        "Signal": signal,
        "SMA20": sma20,
        "SMA50": sma50,
        "RSI": rsi,
    }
    return analyzed
