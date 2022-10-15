import requests
import os
from dotenv import load_dotenv
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


def vk_get_groups(access_token):
    url = f'https://api.vk.com/method/groups.get'
    params = {'access_token': access_token, 'v': '5.131'}
    response = requests.get(url, params=params)  # get json from xkcd.com
    response.raise_for_status()
    user_groups = response.json()
    return user_groups


def get_upload_address(access_token, group_id):
    url = f'https://api.vk.com/method/photos.getWallUploadServer'
    params = {'access_token': access_token, 'group_id': group_id, 'v': '5.131'}
    response = requests.get(url, params=params)
    response.raise_for_status()
    upload_address = response.json()['response']['upload_url']
    return upload_address


def upload_photo_to_server(url_for_upload, group_id, photo, access_token):
    with open(photo, 'rb') as file:
        files = {'photo': file}
        response = requests.post(url_for_upload, files=files)
        response.raise_for_status()
        upload_to_server = response.json()
        server = upload_to_server['server']
        photo = upload_to_server['photo']
        hash = upload_to_server['hash']
        url = 'https://api.vk.com/method/photos.saveWallPhoto'
        response = requests.post(url, {'access_token': access_token,
                                       'group_id': group_id,
                                       'server': server,
                                       'photo': photo,
                                       'hash': hash,
                                       'v': '5.131'})
        response.raise_for_status()
        return response.json()


def main():
    load_dotenv()
    vk_token = os.getenv('VK_USER_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')
    # get_comicbook(353)
    url_for_upload = get_upload_address(vk_token, vk_group_id)
    print(url_for_upload)
    print(upload_photo_to_server(url_for_upload, vk_group_id, 'Files/python.png', vk_token))


if __name__ == '__main__':
    main()
