import requests
import os
import random
import telebot
from dotenv import load_dotenv


def download_first_page():
    url = 'https://xkcd.com/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    first_image = response.json()

    comic_page = first_image['num']
    return comic_page


def download_random_page(path_to_directory, comic_page):
    random_page = random.randint(1, comic_page)
    random_number_url = f'https://xkcd.com/{random_page}/info.0.json'
    response = requests.get(random_number_url)
    response.raise_for_status()

    random_page = response.json()
    random_url = random_page['img']
    img_response = requests.get(random_url)
    img_response.raise_for_status()

    with open(path_to_directory, 'wb') as file:
        file.write(img_response.content)


def upload_to_tgchanel(path_to_directory, telegram_token, channel_id):
    bot = telebot.TeleBot(telegram_token)
    bot.send_photo(channel_id, photo=open(path_to_directory, 'rb'))


def main():
    load_dotenv()

    path_to_directory = os.environ['PATH_TO_DIRECTORY']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    channel_id = os.environ['CHANNEL_ID']

    try:
        first_image = download_first_page()
        random_page = download_random_page(path_to_directory, first_image)
        upload_to_tgchanel(path_to_directory, telegram_token, channel_id)
    except requests.exceptions.RequestException:
        print('Ошибка на стороне телеграмма. Приносим свои извинения')

    finally:
        os.remove(path_to_directory)


if __name__ == '__main__':
    main()
