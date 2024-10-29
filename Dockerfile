# Используем базовый образ Python 3.8
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для Flask API
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]
