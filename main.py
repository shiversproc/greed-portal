"""
main.py - CLI Entry Point
==========================
Run from the terminal to quickly analyze a stock.

Usage:
    python3 main.py AAPL
    python3 main.py TSLA 1y
    python3 main.py SPY 3mo
"""

import sys

from analyzer import analyze


def format_market_cap(cap):
    if cap is None:
        return "N/A"
    if cap >= 1e12:
        return f"${cap / 1e12:.2f}T"
    if cap >= 1e9:
        return f"${cap / 1e9:.2f}B"
    if cap >= 1e6:
        return f"${cap / 1e6:.2f}M"
    return f"${cap:,.0f}"


def main():
    """
    The CLI entry point. Reads args from the terminal, runs the analysis,
    and prints a formatted report.
    """

    if len(sys.argv) < 2:
        print("Usage: python main.py <ticker> [period]")
        sys.exit(1)

    symbol = sys.argv[1]
    period = sys.argv[2] if len(sys.argv) > 2 else "6mo"
    print(f"Fetching data for {symbol}...")
    result = analyze(symbol, period=period)
    print(f"{'=' * 42}\n  {result['Name']} ({result['Symbol']})\n{'=' * 42}")

    for key, value in result.items():
        print(f"  {key}: {value}")
        print(f"{'=' * 42}\n")

if __name__ == "__main__":
    main()
