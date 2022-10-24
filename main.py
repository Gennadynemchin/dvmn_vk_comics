import os
from pathlib import Path
from dotenv import load_dotenv
from xkcd import get_comic_pic, save_comic_pic, get_random_cp_number
from vk import get_upload_address, upload_photo_to_server, publish_wall_post


def main():
    load_dotenv()
    vk_token = os.getenv('VK_USER_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')
    folder = 'Files'

    random_comic_pic, download_url = get_comic_pic(get_random_cp_number())
    saved_comic_pic = save_comic_pic(download_url, folder)
    filepath = Path.cwd() / folder / saved_comic_pic
    try:
        url_for_upload = get_upload_address(vk_token, vk_group_id)
        photo_on_server = upload_photo_to_server(url_for_upload, vk_group_id, filepath, vk_token)
        group_id = f'-{vk_group_id}'
        owner_id = photo_on_server['owner_id']
        media_id = photo_on_server['media_id']
        message = random_comic_pic['comic_pic_comment']
        publish_wall_post(group_id, owner_id, media_id, message, vk_token)
    finally:
        os.remove(os.path.join(folder, saved_comic_pic))


if __name__ == '__main__':
    main()
