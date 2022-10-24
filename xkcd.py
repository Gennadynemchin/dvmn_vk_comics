import random
import requests
import os
from pathlib import Path
from urllib.parse import urlsplit


def get_comic_pic(number_of_comics):
    url = f'https://xkcd.com/{number_of_comics}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response_xkcd = response.json()
    comic_pic_url = response_xkcd['img']
    comic_pic_comment = response_xkcd['alt']
    return comic_pic_comment, comic_pic_url


def save_comic_pic(download_url, folder):
    Path(folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(download_url)
    response.raise_for_status()
    comic_pic_title = urlsplit(download_url).path
    filename = os.path.basename(comic_pic_title)
    filepath = Path.cwd() / folder / filename
    with open(filepath, 'wb') as file:
        file.write(response.content)
    return filename


def get_random_cp_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    max_cp_number = response.json()['num']
    random_number = random.randint(1, max_cp_number)
    return random_number
