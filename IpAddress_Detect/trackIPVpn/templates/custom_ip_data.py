from requests import get



from msvcrt import kbhit
from django import template
    
register = template.Library()  
    
@register.simple_tag
def my_tags():
    # return "Hello World from my_tag() custom template tag."

    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen

    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))