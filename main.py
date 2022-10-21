from dotenv import load_dotenv
from xkcd import *
from vk import *


def main():
    load_dotenv()
    vk_token = os.getenv('VK_USER_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')
    folder = 'Files'

    random_comicbook = get_comicbook(get_random_cb_number(), folder)
    try:
        url_for_upload = get_upload_address(vk_token, vk_group_id)
        upload = upload_photo_to_server(url_for_upload, vk_group_id, f'Files/{random_comicbook["filename"]}', vk_token)
        group_id = f'-{vk_group_id}'
        owner_id = upload['response'][0]['owner_id']
        media_id = upload['response'][0]['id']
        message = random_comicbook['comicbook_comment']
        wall_post(group_id, owner_id, media_id, message, vk_token)
    except KeyError:
        print('No answer from VK server. Check your VK_USER_TOKEN')
    delete_comic_book(folder)
    print(f'The comic book has been posted')


if __name__ == '__main__':
    main()
