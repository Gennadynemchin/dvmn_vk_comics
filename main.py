import requests
import os
from pathlib import Path
from urllib.parse import urlsplit


def get_comicbook(number_of_comics, folder='Files'):
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
    return comicbook_comment


get_comicbook(353)
