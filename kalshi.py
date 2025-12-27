from kalshi_python_sync import Configuration, KalshiClient
from dotenv import load_dotenv
import os
import time

load_dotenv()

def configureClient():
    config = Configuration(
        host="https://api.elections.kalshi.com/trade-api/v2"
    )

    keyPath = os.getenv('KALSHI_PRIVATE_KEY_PATH')
    if keyPath is None:
        raise ValueError("KALSHI_PRIVATE_KEY_PATH is not set")
    with open(keyPath, "r") as f:
        private_key = f.read()

    apikey = os.getenv('KALSHI_API_KEY_ID')
    config.api_key_id = apikey
    config.private_key_pem = private_key

    client = KalshiClient(config)
    return client

client = configureClient()

def getCash():
    balance = client.get_balance()
    return balance.balance/100
    
def getPortfolio():
    balance = client.get_balance()
    return balance.portfolio_value/100    

def get_net_deposits():
    current_val = getCash() * 100
    for x in client.get_settlements().settlements:
        current_val -= x.revenue
    for y in client.get_fills().fills:
        trade_value = (y.price*100) * y.count
        if y.action == 'buy':
            current_val += trade_value
        elif y.action == 'sell':
            current_val -= trade_value
    return current_val / 100

def values():
    return {"cash" : getCash(), "invested" : getPortfolio(), "transferred" : get_net_deposits()}        

def main():
    while True:
        vals = values()
        print("----- Total Current Asset Value: -----")
        print(f"Cash: ${vals['cash']:.2f}")
        print(f"Portfolio: ${vals['invested']:.2f}")
        print("--------------------------------------")
        print(f"Total Deposits: ${vals['transferred']:.2f}")
        time.sleep(1)
    
if __name__ == '__main__':
    main()