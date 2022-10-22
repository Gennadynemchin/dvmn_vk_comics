import random
import requests
import os
from pathlib import Path
from urllib.parse import urlsplit


def get_comicbook(number_of_comics, folder):
    # Path(folder).mkdir(parents=True, exist_ok=True)
    url = f'https://xkcd.com/{number_of_comics}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    url_to_download_comicbook = response.json()['img']
    comicbook_comment = response.json()['alt']
    # response_comicbook = requests.get(url_to_download_comicbook)
    # response_comicbook.raise_for_status()
    # with open(f'{folder}/{filename}', 'wb') as file:
        # file.write(response_comicbook.content)
    return {'comicbook_comment': comicbook_comment,
            'download_url': url_to_download_comicbook}


def save_comicbook(download_url, folder):
    Path(folder).mkdir(parents=True, exist_ok=True)
    response = requests.get(download_url)
    response.raise_for_status()
    comicbook_title = urlsplit(download_url).path
    filename = os.path.basename(comicbook_title)
    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response.content)
    return 'ok'


def delete_comic_book(folder):
    filelist = [f for f in os.listdir(folder)]
    for f in filelist:
        os.remove(os.path.join(folder, f))
    return 'ok'


def get_random_cb_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    max_cb_number = response.json()['num']
    random_number = random.randint(1, max_cb_number)
    return random_number
