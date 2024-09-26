import asyncio
import argparse
import json
from .checker import is_valid_url, check_urls

def main():
    parser = argparse.ArgumentParser(description='CLI-приложение для проверки доступных HTTP-методов для заданных URL.')
    parser.add_argument('strings', metavar='S', type=str, nargs='+', help='Строки для проверки')

    args = parser.parse_args()
    input_strings = args.strings

    valid_urls = []
    for s in input_strings:
        if is_valid_url(s):
            valid_urls.append(s)
        else:
            print(f'Строка "{s}" не является ссылкой.')

    if valid_urls:
        final_result = asyncio.run(check_urls(valid_urls))
        print(json.dumps(final_result, ensure_ascii=False, indent=4))
    else:
        print("Нет допустимых ссылок для проверки.")

if __name__ == '__main__':
    main()
