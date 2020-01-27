import requests
import os

IMAGES_FOLDER = "images"
API_METHOD = "https://api.spacexdata.com/v3/launches"
NAME_PREFIX = "spacex"

def fetch_spacex_last_launch():
    download_photos_from_links(get_latest_spacex_photo_links())

def get_latest_spacex_photo_links():
    image_links = []
    spacex_launches_response = requests.get(API_METHOD)
    if spacex_launches_response.ok:
        for i in range(1,len(spacex_launches_response.json())):
            launch_to_check = len(spacex_launches_response.json()) - i
            image_links = spacex_launches_response.json()[launch_to_check]['links']['flickr_images']
            if image_links:
                break;
    return image_links

def download_photos_from_links(links):
    for link_number, link in enumerate(links):
        image_name = "{}_{}.{}".format(NAME_PREFIX, link_number, get_file_extension_from_link(link))
        save_path = os.path.join(IMAGES_FOLDER, image_name)
        download_image(link, save_path)

def get_file_extension_from_link(link):
    return link.split('.')[-1];

def download_image(url, save_path):
    response = requests.get(url, verify=False)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def main():
    if not os.path.exists(IMAGES_FOLDER):
        os.makedirs(IMAGES_FOLDER)
    fetch_spacex_last_launch()

if __name__ == '__main__':
    main()