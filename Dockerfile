FROM python
WORKDIR .

# Копирование кода в контейнер
COPY . .
COPY requirements.txt .

# Установка зависимостей Python
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
RUN pip3 install -U selenium
RUN pip3 install webdriver-manager

# Запуск тестов
CMD [ "python", "test_adidas.py" ]