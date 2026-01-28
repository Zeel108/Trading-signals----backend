import random
from datetime import datetime

def fetch_zerodha_signals():
    base_price = random.randint(22000, 23000)

    signals = [
        {
            "symbol": "NIFTY",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price,
            "target": base_price + 50,
            "stoploss": base_price - 30,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY1",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY2",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY3",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY5",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY4",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY6",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY7",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        },
        {
            "symbol": "BANKNIFTY8",
            "signal": random.choice(["BUY", "SELL"]),
            "price": base_price + 1200,
            "target": base_price + 1250,
            "stoploss": base_price + 1150,
            "time": datetime.utcnow().isoformat()
        }
    ]
    return signals
