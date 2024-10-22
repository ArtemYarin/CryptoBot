import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException("Валюты не могут быть одинаковы.")

        try:
            quote_ticket = keys[quote]
        except KeyError:
            raise APIException(f"Валюты {quote} нет в списке.")

        try:
            base_ticket = keys[base]
        except KeyError:
            raise APIException(f"Валюты {base} нет в списке.")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Введено неправильное число {amount}.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}")
        total_value = float(json.loads(r.content)[keys[base]]) * float(amount)
        return total_value
