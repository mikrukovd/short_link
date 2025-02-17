import os

from dotenv import load_dotenv
from operations_with_links import is_shorten_link


def main():
    user_input_url = input('Введите ссылку: ')
    load_dotenv()
    token = os.environ('VK_TOKEN')
    print(is_shorten_link(url=user_input_url, token=token))


if __name__ == '__main__':
    main()
