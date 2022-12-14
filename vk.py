import requests


def get_upload_address(access_token, group_id):
    url = f'https://api.vk.com/method/photos.getWallUploadServer'
    params = {'access_token': access_token,
              'group_id': group_id,
              'v': '5.131'}
    response = requests.get(url, params=params)
    response.raise_for_status()
    upload_address = response.json()['response']['upload_url']
    return upload_address


def upload_photo_to_server(url_for_upload, group_id, filepath, access_token):
    with open(filepath, 'rb') as file:
        files = {'photo': file}
        response = requests.post(url_for_upload, files=files)
    response.raise_for_status()
    vk_server_response = response.json()
    server = vk_server_response['server']
    photo = vk_server_response['photo']
    photo_hash = vk_server_response['hash']
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    response = requests.post(url, {'access_token': access_token,
                                   'group_id': group_id,
                                   'server': server,
                                   'photo': photo,
                                   'hash': hash_photo,
                                   'v': '5.131'})
    response.raise_for_status()
    vk_group_response = response.json()
    owner_id = vk_group_response['response'][0]['owner_id']
    media_id = vk_group_response['response'][0]['id']
    return owner_id, media_id


def publish_wall_post(group_id, owner_id, media_id, message, access_token):
    attachments = f'photo{owner_id}_{media_id}'
    group_id = f'-{group_id}'
    url = 'https://api.vk.com/method/wall.post'
    response = requests.post(url, {'from_group': 1,
                                   'owner_id': group_id,
                                   'v': '5.131',
                                   'access_token': access_token,
                                   'message': message,
                                   'attachments': attachments})
    response.raise_for_status()
    return response.json()
