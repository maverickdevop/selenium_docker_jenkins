FROM python
WORKDIR .

# Копирование кода в контейнер
COPY . .
COPY requirements.txt .

# Установка зависимостей Python
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

# Запуск тестов
CMD python3 -m pytest -sv test_adidas.py