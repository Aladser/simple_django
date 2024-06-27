import os.path

from django import template

from config.settings import BASE_DIR

register = template.Library()
IMG_FOLDER = 'media/img'


@register.filter()
def full_image_path(image_file):
    img_folder_url = f"/{IMG_FOLDER}/"
    if image_file != '' and os.path.isfile(BASE_DIR / IMG_FOLDER / str(image_file)):
        return img_folder_url + str(image_file)
    else:
        return img_folder_url + 'empty_file.png'
