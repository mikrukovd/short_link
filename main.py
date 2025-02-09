import os
import requests

from dotenv import load_dotenv
from operations_with_links import shorten_link, count_clicks, is_shorten_link


def main():
    url = input('Введите ссылку: ')
    load_dotenv()
    token = os.getenv('API')

    if is_shorten_link(url=url):
        try:
            count_link = count_clicks(link=url, token=token)
            print('Количество переходов по ссылке:', count_link)
        except requests.exceptions.HTTPError as http_error:
            print(http_error)
    else:
        try:
            short_url = shorten_link(url=url, token=token)
            print('Короткая ссылка:', short_url)
        except requests.exceptions.HTTPError as http_error:
            print({http_error})


if __name__ == '__main__':
    main()
