import requests
import os
from utils import download_image
from string import Template

IMAGES_FOLDER = "images"
API_COLLECTION_METHOD = "http://hubblesite.org/api/v3/images?page=all&collection_name="
API_PHOTOS_METHOD = "http://hubblesite.org/api/v3/image/"
NAME_PREFIX = "hubble"
COLLECTION_NAME = "stsci_gallery"
API_REQUEST_TEMPLATE = Template("$api_method$arg")

def fetch_hubble_photos_from_collection(collection_name):
    api_request = API_REQUEST_TEMPLATE.substitute(api_method = API_COLLECTION_METHOD, arg = collection_name)
    api_response = requests.get(api_request)
    if api_response.ok:
        for photo in api_response.json():
            fetch_best_hubble_photo_by_id(photo["id"])
    else:
        return

def fetch_best_hubble_photo_by_id(id):
    best_photo_link = get_hubble_photo_links_by_id(id)[-2]
    image_file_extension = os.path.splitext(best_photo_link)[1]
    image_name = f"{NAME_PREFIX}_{id}{image_file_extension}"
    save_path = os.path.join(IMAGES_FOLDER, image_name)
    download_image(best_photo_link, save_path)

def get_hubble_photo_links_by_id(id):
    image_links = []
    api_request = API_REQUEST_TEMPLATE.substitute(api_method = API_PHOTOS_METHOD, arg = str(id));
    api_response = requests.get(api_request)
    if api_response.ok:
        for file in api_response.json()['image_files']:
            image_links.append(f"http:{file['file_url']}")
    return image_links

def main():
    os.makedirs(IMAGES_FOLDER, exist_ok = True)
    fetch_hubble_photos_from_collection(COLLECTION_NAME)

if __name__ == '__main__':
    main()