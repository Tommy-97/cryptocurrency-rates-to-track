import time
from threading import Thread

from config import CHECK_INTERVAL
from handlers import bot, send_notification, thresholds
from tracker import get_crypto_price


def track_prices():
    """Отслеживание курсов криптовалют и отправка уведомлений."""
    while True:
        for chat_id, user_thresholds in thresholds.items():
            for symbol, (min_price, max_price) in user_thresholds.items():
                try:
                    price = get_crypto_price(symbol)
                    if price <= min_price:
                        send_notification(
                            chat_id, symbol, price, "минимального")
                    elif price >= max_price:
                        send_notification(
                            chat_id, symbol, price, "максимального")
                except Exception as e:
                    print(f"Ошибка отслеживания {symbol}: {e}")
        time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    # Запуск отслеживания в отдельном потоке
    tracking_thread = Thread(target=track_prices, daemon=True)
    tracking_thread.start()

    # Запуск бота
    bot.polling(none_stop=True)
