from kalshi_python_sync import Configuration, KalshiClient
from dotenv import load_dotenv
import os

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
balance = client.get_balance()
print(f"Balance: ${balance.balance / 100:.2f}")