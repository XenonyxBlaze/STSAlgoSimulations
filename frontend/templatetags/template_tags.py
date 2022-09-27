from django import template

register = template.Library()

@register.filter
def at_index(data, index):
    return data[index]