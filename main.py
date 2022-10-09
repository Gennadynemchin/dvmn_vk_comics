import requests
import os
import posixpath
import urllib.parse
from pathlib import Path


def get_comics(number_of_comics, folder):
    Path(folder).mkdir(parents=True, exist_ok=True)
    filename = 'python_comics.png'
    url = f'https://xkcd.com/{number_of_comics}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    decoded_response = response.json()
    url_to_download_comics = decoded_response['img']
    response_comics = requests.get(url_to_download_comics)
    response_comics.raise_for_status()
    filename = os.path.basename(filename)
    comics_comment = decoded_response['alt']
    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response_comics.content)
    return comics_comment


print(get_comics(353, 'Files'))
