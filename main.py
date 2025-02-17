import os
import requests

from dotenv import load_dotenv
from operations_with_links import shorten_link, is_shorten_link, count_clicks


def main():
    load_dotenv()
    token = os.environ['VK_TOKEN']
    user_input_url = input('Введите ссылку: ')

    if is_shorten_link(user_input_url, token):
        try:
            print(f'Количество переходов по ссылке: {count_clicks(user_input_url, token)}')
        except requests.exceptions.HTTPError as http_error:
            print(http_error)
    else:
        try:
            print(f'Короткая ссылка: {shorten_link(user_input_url, token)}')
        except requests.exceptions.HTTPError as http_error:
            print(http_error)


if __name__ == '__main__':
    main()
