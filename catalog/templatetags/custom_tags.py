import datetime
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def current_time(format_string='%H:%M:%Y'):
    return datetime.datetime.now().strftime(format_string)


@register.filter()
def title_filter(text):
    return mark_safe(f"<span>{text.title()}</span>")
