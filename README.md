# URL Checker

**URL Checker** — это CLI-приложение для проверки доступных HTTP-методов для заданных URL-адресов. Приложение асинхронно проверяет каждый URL и определяет, какие HTTP-методы доступны, а затем выводит результаты в формате JSON.

## Содержание

- [Установка](#Установка)
- [Использование](#Использование)
- [Использование в качестве модуля](#Использование-в-качестве-модуля)
- [Тестирование](#Тестирование)
- [Требования](#Требования)
- [Зависимости](#Зависимости)
- [Структура проекта](#Структура-проекта)
- [Автор](#Автор)
- [Контактная информация](#Контактная-информация)

## Установка

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Runya1337/Test_Nagornaya
2. **Перейдите в каталог проекта:**
   ```bash
   cd url_checker
3. **Установите зависимости и сам пакет:**
   ```bash
   pip install .
## Использование

После установки вы можете использовать команду url_checker в терминале:
```bash 
url_checker https://google.com https://www.facebook.com wrongstring
```
Пример вывода:

```bash
Строка "wrongstring" не является ссылкой.
{
    "https://google.com": {
        "GET": 301,
        "HEAD": 301
    },
    "https://www.facebook.com": {
        "GET": 200,
        "HEAD": 200,
        "OPTIONS": 200
    }
}
```
## Использование в качестве модуля

Вы также можете импортировать url_checker в свои Python-скрипты:

```python
from url_checker import is_valid_url, check_urls
import asyncio

input_strings = ['https://google.com', 'https://www.facebook.com', 'notalink']
valid_urls = [url for url in input_strings if is_valid_url(url)]

if valid_urls:
    final_result = asyncio.run(check_urls(valid_urls))
    print(final_result)
else:
    print("Нет допустимых ссылок для проверки.")
```
## Тестирование

Установите зависимости для тестирования:

```bash
pip install -r requirements.txt
pip install pytest pytest-asyncio coverage
```
Запустите тесты и сгенерируйте отчёт о покрытии:

```bash
coverage run -m pytest
coverage report -m
```
Пример отчёта о покрытии:
```bash
Name                         Stmts   Miss  Cover
------------------------------------------------
url_checker/__init__.py           1      0   100%
url_checker/checker.py           28      0   100%
url_checker/cli.py               19      0   100%
tests/test_checker.py            49      0   100%
------------------------------------------------
TOTAL                            97      0   100%
```
## Требования

Python 3.7 или выше
aiohttp>=3.7.4
## Зависимости

Все зависимости указаны в файле requirements.txt.

## Структура проекта

```arduino
Copy code
url_checker/
├── url_checker/
│   ├── __init__.py
│   ├── checker.py
│   └── cli.py
├── tests/
│   └── test_checker.py
├── setup.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Автор

Имя - Nurtdinov Ainur

## Контактная информация
**Email**:  Ainurnurtdinov1337@gmail.com

**GitHub** :    https://github.com/Runya1337
