# Auto post vk.com

The script is getting a random comic book from the https://xkcd.com.
After that it posts on the https://vk.com wall of your community.

## Environment

You have to change some variables in .env:
```
VK_APP_CLIENT_ID=YOUR_VK_APP_ID
VK_USER_ID=YOUR_USER_ID
VK_GROUP_ID=GROUP_ID_FOR_POSTING
VK_USER_TOKEN=YOUR_VK_TOKEN
```
Please see how to get your vk app id here: https://dev.vk.com 

As far as the https://vk.com doesn't allow to get vk token by API request
(at least officially) you have to sign in to https://vk.com,
then open the following link on your browser:

https://oauth.vk.com/authorize?client_id={VK_APP_CLIENT_ID}&display=mobile&scope=photos,groups,wall&response_type=token&v=5.131

After that you will be redirected to new link where you have to copy your token.
Unfortunately it expires in 86400 seconds.

### How to install

Clone the project:
```
git clone https://github.com/Gennadynemchin/dvmn_vk_comics.git
cd dvmn_vk_comics
```
Create and activate a virtual environment:
```
python3 -m venv env
source env/bin/activate
```
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## How to run

For starting the script please run on command line: 
```
python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
