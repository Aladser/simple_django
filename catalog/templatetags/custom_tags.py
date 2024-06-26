from django import template

register = template.Library()


@register.filter()
def full_image_path(image_file):
    return '/media/img/'+str(image_file)
