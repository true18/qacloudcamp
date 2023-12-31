# Автоматизация тестирования API

Проект содержит автоматические тесты для проверки работы API. Тесты написаны на Python с использованием библиотек `pytest` и `requests`

## Требования

- Python 3.10
- Docker (для запуска тестов в контейнере)

## Установка


1. Перейдите в директорию проекта:

    ```sh
    cd <директория проекта>
    ```

2. Установите необходимые библиотеки:

    ```sh
    pip install pytest requests
    ```

## Запуск тестов

Для запуска тестов выполните следующую команду:

```sh
pytest main_test.py
```

## Запуск тестов с использованием Docker

1. Убедитесь, что у вас установлен Docker.

2. Перейдите в корневую директорию проекта.

3. Соберите Docker-образ с помощью следующей команды:

    ```sh
    docker build -t api-tests .
    ```

4. Запустите тесты внутри Docker-контейнера с помощью следующей команды:

    ```sh
    docker run --rm api-tests
    ```