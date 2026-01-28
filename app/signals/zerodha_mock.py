import random
from datetime import datetime, timedelta
import json

STOCKS = [
    {"symbol": "AAPL", "name": "Apple Inc."},
    {"symbol": "MSFT", "name": "Microsoft Corp."},
    {"symbol": "GOOGL", "name": "Alphabet Inc."},
    {"symbol": "AMZN", "name": "Amazon.com Inc."},
    {"symbol": "TSLA", "name": "Tesla Inc."},
    {"symbol": "FB", "name": "Meta Platforms"},
    {"symbol": "NVDA", "name": "NVIDIA Corp."},
    {"symbol": "JPM", "name": "JPMorgan Chase"},
    {"symbol": "V", "name": "Visa Inc."},
    {"symbol": "DIS", "name": "Walt Disney Co."},
    {"symbol": "NFLX", "name": "Netflix Inc."},
    {"symbol": "PYPL", "name": "PayPal Holdings"},
    {"symbol": "ADBE", "name": "Adobe Inc."},
    {"symbol": "INTC", "name": "Intel Corp."},
    {"symbol": "CSCO", "name": "Cisco Systems"},
    {"symbol": "ORCL", "name": "Oracle Corp."},
    {"symbol": "CRM", "name": "Salesforce"},
    {"symbol": "KO", "name": "Coca-Cola Co."},
    {"symbol": "PEP", "name": "PepsiCo Inc."},
    {"symbol": "MCD", "name": "McDonald's Corp."},
    {"symbol": "BA", "name": "Boeing Co."},
    {"symbol": "GE", "name": "General Electric"},
    {"symbol": "IBM", "name": "IBM Corp."},
    {"symbol": "NKE", "name": "Nike Inc."},
    {"symbol": "SBUX", "name": "Starbucks Corp."},
    {"symbol": "VZ", "name": "Verizon Communications"},
    {"symbol": "T", "name": "AT&T Inc."},
    {"symbol": "XOM", "name": "Exxon Mobil Corp."},
    {"symbol": "CVX", "name": "Chevron Corp."},
    {"symbol": "WMT", "name": "Walmart Inc."}
]

def generate_zerodha_signals():
    base_date = datetime.now()
    signals = []
    for stock in STOCKS:
        signals.append({
            "symbol": stock["symbol"],
            "name": stock["name"],
            "price": round(random.uniform(50, 500), 2),
            "prChange": round(random.uniform(-5, 5), 2),
            "percChange": round(random.uniform(-2, 2), 2),
            "rsi": round(random.uniform(10, 90), 2),
            "macd": round(random.uniform(-5, 5), 2),
            "date": (base_date - timedelta(days=random.randint(0, 10))).strftime("%Y-%m-%d")
        })
    return signals

# test print
if __name__ == "__main__":
    print(json.dumps(generate_zerodha_signals(), indent=2))
