import requests
import os
from utils import download_image

IMAGES_FOLDER = "images"
API_METHOD = "https://api.spacexdata.com/v3/launches"
NAME_PREFIX = "spacex"

def fetch_spacex_last_launch():
    download_photos_from_links(get_latest_spacex_photo_links())

def get_latest_spacex_photo_links():
    image_links = []
    spacex_launches_response = requests.get(API_METHOD)
    if spacex_launches_response.ok:
        spacex_launches_response_decoded = spacex_launches_response.json();
        for i in range(1,len(spacex_launches_response_decoded)):
            launch_to_check = len(spacex_launches_response_decoded) - i
            image_links = spacex_launches_response_decoded[launch_to_check]['links']['flickr_images']
            if image_links:
                break;
    return image_links

def download_photos_from_links(links):
    for link_number, link in enumerate(links):
        image_file_extension = os.path.splitext(link)[1]
        image_name = f"{NAME_PREFIX}_{link_number}{image_file_extension}"
        save_path = os.path.join(IMAGES_FOLDER, image_name)
        download_image(link, save_path)

def main():
    os.makedirs(IMAGES_FOLDER, exist_ok = True)
    fetch_spacex_last_launch()

if __name__ == '__main__':
    main()