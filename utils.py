import requests
import os

def download_image(url, save_path):
    response = requests.get(url, verify=False)
    with open(save_path, 'wb') as file:
        file.write(response.content)