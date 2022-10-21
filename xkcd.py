import random
import requests
import os
from pathlib import Path
from urllib.parse import urlsplit


def get_comicbook(number_of_comics, folder):
    Path(folder).mkdir(parents=True, exist_ok=True)  # settings for comics directory creating
    url = f'https://xkcd.com/{number_of_comics}/info.0.json'
    response = requests.get(url)  # get json from xkcd.com
    response.raise_for_status()
    url_to_download_comicbook = response.json()['img']  # get comics url from xkcd.com json
    comicbook_comment = response.json()['alt']  # get comics comment from json
    response_comicbook = requests.get(url_to_download_comicbook)  # request a path for download a comics
    response_comicbook.raise_for_status()
    comicbook_title = urlsplit(url_to_download_comicbook).path  # get current comics title
    filename = os.path.basename(comicbook_title)  # creating filename from comics url

    with open(f'{folder}/{filename}', 'wb') as file:  # writing the comics to directory
        file.write(response_comicbook.content)
    return {'comicbook_comment': comicbook_comment, 'filename': filename}


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
