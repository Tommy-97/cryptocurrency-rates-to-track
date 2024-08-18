# Dockerfile

# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем весь код
COPY bot/ ./bot/

# Команда запуска
CMD ["python", "bot/main.py"]
