import requests

from bot.config import API_KEY, CMC_URL


def get_crypto_price(symbol):
    """Запрос курса криптовалюты с API CoinMarketCap."""
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    params = {
        'symbol': symbol,
        'convert': 'USD'
    }

    try:
        response = requests.get(CMC_URL, headers=headers, params=params)
        response.raise_for_status()  # Проверка на HTTP ошибки

        data = response.json()

        if 'data' in data and symbol in data['data']:
            return data['data'][symbol]['quote']['USD']['price']
        else:
            raise ValueError(f"Ошибка: данные для {symbol} не найдены.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети или API: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Ошибка обработки данных: {e}")
        return None
