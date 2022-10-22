import random
import requests
import os
from pathlib import Path
from urllib.parse import urlsplit


def get_comic_pic(number_of_comics):
    url = f'https://xkcd.com/{number_of_comics}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    url_to_download_comic_pic = response.json()['img']
    comic_pic_comment = response.json()['alt']
    return {'comic_pic_comment': comic_pic_comment,
            'download_url': url_to_download_comic_pic}


def save_comic_pic(download_url, folder):
    Path(folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(download_url)
    response.raise_for_status()
    comic_pic_title = urlsplit(download_url).path
    filename = os.path.basename(comic_pic_title)
    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response.content)
    return filename


def delete_comic_pic(folder, filename):
    os.remove(os.path.join(folder, filename))
    return 'ok'


def get_random_cp_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    max_cp_number = response.json()['num']
    random_number = random.randint(1, max_cp_number)
    return random_number
