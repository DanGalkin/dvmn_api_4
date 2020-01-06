import requests
import os

def download_image(url, file_name):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(file_name, 'wb') as file:
        file.write(response.content)

def download_photos(links, photos_name, folder_name):
	if not os.path.exists(folder_name):
		os.makedirs(folder_name)
	for link_number, link in enumerate(links):
		file_name = "{}/{}{}.{}".format(folder_name, photos_name, link_number, get_file_extension(link))
		download_image(link, file_name)

def get_file_extension(link):
	return link.split('.')[-1];

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

def fetch_spacex_last_launch():
	download_photos(get_latest_spacex_photo_links(), "spacex", "images")

def get_hubble_photo_links(id):
	api_method = "http://hubblesite.org/api/v3/image/"
	api_request = api_method + str(id);
	image_links = []
	image_api_response = requests.get(api_request)
	if image_api_response.ok:
		for file in image_api_response.json()['image_files']:
			image_links.append("http:"+file['file_url'])
	return image_links

def fetch_hubble_photo(id):
	best_image = [get_hubble_photo_links(id)[-1]]
	download_photos(best_image, "hubble_" + str(id), "images")

def get_hubble_photos_from_collection(collection):
	api_method = "http://hubblesite.org/api/v3/images?page=all&collection_name="
	api_request = api_method + collection;
	collection_api_response = requests.get(api_request)
	if collection_api_response.ok:
		for photo in collection_api_response.json():
			fetch_hubble_photo(photo["id"])
			#debug print
			print("Downloading picture id: " + str(photo["id"]))
	else:
		print("No such collection in Hubble API.")

def main():
    get_hubble_photos_from_collection("printshop")

if __name__ == '__main__':
    main()