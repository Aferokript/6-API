import requests
import os


def install_python_comic():
    comic_directory = r'C:\Users\Admin\Python\comics'
    os.makedirs(comic_directory, exist_ok=True)

    save_pycomic_directory = os.path.join(comic_directory, 'comics')

    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()

    data = response.json()
    comic_url = data['img']
    img_response = requests.get(comic_url)
    with open(save_pycomic_directory, 'wb') as file:
        file.write(img_response.content)
    print("Комикс сохранен как comic.png")

install_python_comic()



