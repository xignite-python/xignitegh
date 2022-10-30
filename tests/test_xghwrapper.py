import requests

from xghwrapper import Stock


def test_stock_info():
    token_data = get_token()
    msft = Stock("MSFT", **token_data)
    response = msft.info()
    assert isinstance(response, dict)
    assert response["Symbol"] == "MSFT"


def get_token():
    response = requests.get("https://seekingalpha.com/market_data/xignite_token")
    return response.json()
