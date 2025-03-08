# Базовый образ Python
FROM python:3.11

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода
COPY . .

# Указание порта
EXPOSE 5000

# Команда запуска
CMD ["python3", "app_server/app.py"]
