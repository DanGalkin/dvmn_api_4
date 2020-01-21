# dvmn_api_4

### Description

Set of scripts to download photos from SpaceX and Hubble APIs and upload them to Instagram.

- **fetch_hubble.py** downloads best .jpg images from Hubble "stsci_gallery" photo collection (you can modify global variable *COLLECTION_NAME* to try dofferent collections like "holiday_cards", "wallpaper", "spacecraft", "news", "printshop")
- **fetch_spacex.py** downloads latest available photos of the SpaceX launches
- **crop_and_publish.py** crops images in a folder to a square and publishes it to instagram using your credentials


### How to install
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

To use **crop_and_publish.py** you need to store your Instagram account credentials in the .env file as shown below:
```
INSTAGRAM_LOGIN=*your_login*
INSTAGRAM_PASSWORD=*your_password*
```
Locate the .env file in the same folder with **crop_and_publish.py**.


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).