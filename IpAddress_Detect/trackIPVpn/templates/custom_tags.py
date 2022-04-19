from msvcrt import kbhit
from django import template
    
register = template.Library()  
    
@register.simple_tag
def my_tag():
    # return "Hello World from my_tag() custom template tag."

    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen

    ip = '106.202.225.196'
    api_key = 'at_lq8wRnoBrBT2YrgzIUNaSeoVxN3ym&'
    api_url = 'https://geo.ipify.org/api/v1?'

    url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip

    # print()
    k = urlopen(url).read().decode('utf8')
    return k
    print("Hooray!!")