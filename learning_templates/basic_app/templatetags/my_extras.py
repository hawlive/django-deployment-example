from django import template

# Create your views here.
register = template.Library()

@register.filter(name='cut')

def cut(value,arg):
    """
    This cuts our all values of "arg" from the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)