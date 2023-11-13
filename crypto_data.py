import requests
from dataclasses import dataclass
from typing import Final


BASE_URL: Final[str] = "https://api.coingecko.com/api/v3/coins/markets"


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float


def get_coins() -> list[Coin]:
    """
    Gets coins from an api and returns them as a list[Coin]
    API: https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur

    """
    payload: list = {'vs_currency': 'eur', 'order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    jsonData: dict = data.json()

    # Create coins and add them to a coin list
    coins_list: list[Coin] = []
    for item in jsonData:
        current_coin: Coin = Coin(name=item.get("name"),
                                  symbol=item.get('symbol'),
                                  current_price=item.get('current_price'),
                                  high_24h=item.get('high_24h'),
                                  low_24h=item.get('low_24h'),
                                  price_change_24h=item.get(
                                      'price_change_24h'),
                                  price_change_percentage_24h=item.get('price_change_percentage_24h'))

        coins_list.append(current_coin)
    return coins_list


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):

    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                # Add the code you want to be executed if a coin reaches
                print(coin, '!!!TRIGGER!!!')
            else:
                print(coin)


if __name__ == "__main__":
    coins: list[Coin] = get_coins()
    alert('btc', bottom=10, top=20_000, coins_list=coins)

    # # Create a loop for these to create live alerts
    # alert('btc', bottom=10, top=20_000, coins_list=coins)
    # alert('eth', bottom=10, top=20_000, coins_list=coins)
    # alert('xrp', bottom=0.47, top=0.48, coins_list=coins)
