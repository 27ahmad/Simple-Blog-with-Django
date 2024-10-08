from django import template
import re

register = template.Library()

@register.filter(name='strip_tags')
def strip_tags(value):
    """
    Strips HTML tags from a string.
    """
    return re.sub(r'<.*?>', '', value)  # Regular expression to remove HTML tags
