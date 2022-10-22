import os
from dotenv import load_dotenv
from xkcd import get_comic_pic, save_comic_pic, delete_comic_pic, get_random_cp_number
from vk import get_upload_address, upload_photo_to_server, wall_post


def main():
    load_dotenv()
    vk_token = os.getenv('VK_USER_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')
    folder = 'Files'

    random_comicbook = get_comic_pic(get_random_cp_number())
    saved_comicbook = save_comic_pic(random_comicbook['download_url'], folder)
    url_for_upload = get_upload_address(vk_token, vk_group_id)
    upload = upload_photo_to_server(url_for_upload, vk_group_id, f'Files/{saved_comicbook}', vk_token)
    group_id = f'-{vk_group_id}'
    owner_id = upload['response'][0]['owner_id']
    media_id = upload['response'][0]['id']
    message = random_comicbook['comicbook_comment']
    wall_post(group_id, owner_id, media_id, message, vk_token)
    delete_comic_pic(folder)


if __name__ == '__main__':
    main()
