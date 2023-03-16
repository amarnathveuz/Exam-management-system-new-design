# myapp/templatetags/my_filters.py
from django import template

register = template.Library()

@register.filter
def getattr(obj, attr):
    print("helllllllllllllllllllll")
    return getattr(obj, attr)


