import requests
import os

IMAGES_FOLDER = "images"
API_COLLECTION_METHOD = "http://hubblesite.org/api/v3/images?page=all&collection_name="
API_PHOTOS_METHOD = "http://hubblesite.org/api/v3/image/"
NAME_PREFIX = "hubble"
COLLECTION_NAME = "stsci_gallery"

def fetch_hubble_photos_from_collection(collection_name):
    api_request = API_COLLECTION_METHOD + collection_name;
    api_response = requests.get(api_request)
    if api_response.ok:
        for photo in api_response.json():
            fetch_best_hubble_photo_by_id(photo["id"])
    else:
        print("No such collection in Hubble API.")

def fetch_best_hubble_photo_by_id(id):
    best_photo_link = get_hubble_photo_links_by_id(id)[-2]
    save_path = "{}/{}_{}.{}".format(IMAGES_FOLDER, NAME_PREFIX, str(id), get_file_extension_from_link(best_photo_link))
    download_image(best_photo_link, save_path)

def get_hubble_photo_links_by_id(id):
    image_links = []
    api_request = API_PHOTOS_METHOD + str(id);
    api_response = requests.get(api_request)
    if api_response.ok:
        for file in api_response.json()['image_files']:
            image_links.append("http:"+file['file_url'])
    return image_links

def get_file_extension_from_link(link):
    return link.split('.')[-1];

def download_image(url, save_path):
    response = requests.get(url, verify=False)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def main():
    if not os.path.exists(IMAGES_FOLDER):
        os.makedirs(IMAGES_FOLDER)
    fetch_hubble_photos_from_collection(COLLECTION_NAME)

if __name__ == '__main__':
    main()