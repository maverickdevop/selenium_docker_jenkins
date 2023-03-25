FROM python:3.9-slim-buster

# Копирование кода в контейнер
WORKDIR /app
COPY . .

# Установка зависимостей Python
RUN pip install -r requirements.txt

# Запуск тестов
CMD python3 -m pytest -sv tests/*