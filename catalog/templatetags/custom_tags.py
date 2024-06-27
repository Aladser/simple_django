import os.path

from django import template

from config.settings import BASE_DIR

register = template.Library()


@register.filter()
def full_image_path(image_file):
    img_folder_path = '/media/img/'
    full_path = img_folder_path + str(image_file)

    if image_file != '':
        return full_path
    else:
        return img_folder_path + 'empty_file.png'
