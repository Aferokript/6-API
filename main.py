import requests
import os
import random
import telebot
from dotenv import load_dotenv


def install_random_pycomic():
    url = 'https://xkcd.com/info.0.json'

    comic_directory = r'C:\Users\Admin\Python\comics'
    os.makedirs(comic_directory, exist_ok=True)

    save_pycomic_directory = os.path.join(comic_directory, 'comics')

    response = requests.get(url)
    response.raise_for_status()

    first_image = response.json()
    comic_url = first_image['img']
    comic_page = first_image['num']
    random_page = random.randint(1, comic_page)
    random_number_url = f'https://xkcd.com/{random_page}/info.0.json'
    response = requests.get(random_number_url)
    response.raise_for_status()

    random_page = response.json()
    random_image = random_page['img']
    img_response = requests.get(random_image)
    with open(save_pycomic_directory, 'wb') as file:
        file.write(img_response.content)
    


def upload_to_telegram(telegram_token, chanel_id):
    bot = telebot.TeleBot(telegram_token)
    install_random_pycomic()
    bot.send_photo(chanel_id, photo=open(r'C:\Users\Admin\Python\comics\comics', 'rb'))


def main():
    load_dotenv()

    telegram_token = os.getenv('TELEGRAM_TOKEN')
    chanel_id = os.getenv('CHANEL_ID')


    upload_to_telegram(telegram_token, chanel_id)
    os.remove(r'C:\Users\Admin\Python\comics\comics')


if __name__ == '__main__':
    main()


