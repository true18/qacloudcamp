# Используем Python
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в рабочую директорию контейнера
COPY . /app

# Устанавливаем необходимые библиотеки
RUN pip install --no-cache-dir pytest requests

# Запускаем тесты при старте контейнера
CMD ["pytest", "main_test.py"]
