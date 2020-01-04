import requests
import os

def download_image(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def get_latest_spacex_photo_links():
    api_method = "https://api.spacexdata.com/v3/launches"
    image_links = []
    spacex_launches_response = requests.get(api_method)
    if spacex_launches_response.ok:
        for i in range(1,len(spacex_launches_response.json())):
            launch_to_check = len(spacex_launches_response.json()) - i
            image_links = spacex_launches_response.json()[launch_to_check]['links']['flickr_images']
            if image_links:
                break;
    return image_links

def download_photos(links, photos_name, folder_name, format_name):
	if not os.path.exists(folder_name):
		os.makedirs(folder_name)
	for link_number, link in enumerate(links):
		file_name = "{}/{}{}.{}".format(folder_name, photos_name, link_number, format_name)
		download_image(link, file_name)

def fetch_spacex_last_launch():
	download_photos(get_latest_spacex_photo_links(), "spacex", "images", "jpg")

def main():
    fetch_spacex_last_launch()

if __name__ == '__main__':
    main()