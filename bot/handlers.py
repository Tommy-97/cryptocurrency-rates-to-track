from telebot import TeleBot

from bot.config import TELEGRAM_TOKEN
from bot.tracker import get_crypto_price

bot = TeleBot(TELEGRAM_TOKEN)

# Хранилище пороговых значений и chat_id для каждого пользователя
thresholds = {}


@bot.message_handler(commands=['start', 'set'])
def handle_command(message):
    chat_id = message.chat.id
    try:
        _, symbol, min_price, max_price = message.text.split()
        symbol = symbol.upper()
        thresholds[chat_id] = thresholds.get(chat_id, {})
        thresholds[chat_id][symbol] = (float(min_price), float(max_price))
        bot.send_message(
            chat_id, f'Отслеживание {symbol} установлено. Мин: ${min_price}, Макс: ${max_price}')
    except Exception as e:
        bot.send_message(
            chat_id, 'Ошибка! Используйте формат: /set BTC 30000 50000')


def send_notification(chat_id, symbol, price, threshold_type):
    """Отправка уведомления в Telegram."""
    bot.send_message(
        chat_id, f'{symbol} достиг {threshold_type} порога: ${price:.2f}')


def check_prices():
    """Проверка цен и отправка уведомлений при необходимости."""
    for chat_id, user_thresholds in thresholds.items():
        for symbol, (min_price, max_price) in user_thresholds.items():
            price = get_crypto_price(symbol)
            if price <= min_price:
                send_notification(chat_id, symbol, price, 'нижнего')
            elif price >= max_price:
                send_notification(chat_id, symbol, price, 'верхнего')


# Запуск polling для приема сообщений
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
