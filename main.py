import os
import requests
import argparse

from dotenv import load_dotenv
from operations_with_links import shorten_link, is_shorten_link, count_clicks


def main():
    load_dotenv()
    token = os.environ['VK_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()
    inputed_url = args.url

    if is_shorten_link(inputed_url, token):
        try:
            print(f'Количество переходов по ссылке: {count_clicks(token, inputed_url)}')
        except requests.exceptions.HTTPError as http_error:
            print(http_error)
    else:
        try:
            print(f'Короткая ссылка: {shorten_link(inputed_url, token)}')
        except requests.exceptions.HTTPError as http_error:
            print(http_error)


if __name__ == '__main__':
    main()
