import requests
from urllib.parse import urlparse


def shorten_link(url, token):
    short = 'https://api.vk.ru/method/utils.getShortLink'
    params = {
        'access_token': token,
        'v': 5.199,
        'url': url
    }
    response = requests.get(short, params=params)
    response.raise_for_status()
    short_link = response.json()

    if 'error' in short_link:
        error_code = short_link['error']['error_code']
        error_msg = short_link['error']['error_msg']
        raise requests.exceptions.HTTPError(f'Error {error_code}: {error_msg}')

    return short_link['response']['short_url']


def count_clicks(token, link):
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    parsed_link = urlparse(link)
    key = parsed_link.path[1:]
    params = {
        'access_token': token,
        'v': 5.199,
        'key': key,
        'extended': 0,
        'interval': 'forever'
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    clicks_count = response.json()

    if 'error' in clicks_count:
        error_code = clicks_count['error']['error_code']
        error_msg = clicks_count['error']['error_msg']
        raise requests.exceptions.HTTPError(f'Error {error_code}: {error_msg}')

    return clicks_count['response']['stats'][0]['views']


def is_shorten_link(url, token):
    try:
        return f'Количество переходов по ссылке: {count_clicks(token, link=url)}'
    except requests.exceptions.HTTPError:
        return f'Короткая ссылка: {shorten_link(url=url, token=token)}'
