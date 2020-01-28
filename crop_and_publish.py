import os
from os import listdir
from os.path import isfile, join
from PIL import Image
from dotenv import load_dotenv
from instabot import Bot

IMAGES_FOLDER = "images"

def publish_to_instagram_from_folder(folder_path, credentials):
    bot = Bot()
    bot.login(username=credentials[0], password=credentials[1])
    for image in get_folder_files_list(folder_path):
        image_path = join(folder_path, image)
        crop_image_to_square(image_path)
        bot.upload_photo(image_path, options={"rename": False})

def get_folder_files_list(folder_path):
    files = []
    for child in listdir(folder_path):
        child_path = join(folder_path, child)
        if isfile(child_path):
            files.append(child)
    return files

def crop_image_to_square(image_path):
    image = Image.open(image_path)
    crop_left = 0;
    crop_up = 0;
    crop_right = 0;
    crop_down = 0;
    if image.width > image.height:
        crop_left = int((image.width - image.height)/2);
        crop_right = image.width - image.height - crop_left;
    elif image.height > image.width:
        crop_up = int((image.height - image.width)/2)
        crop_down = image.height - image.width - crop_up;
    else:
        return
    crop_coordinates = (crop_left, crop_up, image.width - crop_right, image.height - crop_down)
    cropped_image = image.crop(crop_coordinates)
    cropped_image.save(image_path)

def main():
    instagram_credentials = (os.getenv("INSTAGRAM_LOGIN"), os.getenv("INSTAGRAM_PASSWORD"))
    publish_to_instagram_from_folder(IMAGES_FOLDER, instagram_credentials);

if __name__ == '__main__':
    load_dotenv()
    main()