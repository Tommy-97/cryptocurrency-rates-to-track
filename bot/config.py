# bot/config.py
import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


# Токен для Telegram бота
TELEGRAM_TOKEN = os.getenv(
    'TELEGRAM_TOKEN', '6919499560:AAEjBDAyIzFyRdgExOsXThMWDEn59mIMSbU')

# API ключ CoinMarketCap
API_KEY = os.getenv('API_KEY', 'dc99b749-b6b6-4068-8fab-a130e6a5dc5b')

# URL для получения данных о криптовалютах
CMC_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Интервал проверки (в секундах)
CHECK_INTERVAL = 60
