from django import template
from django.template.defaultfilters import stringfilter

from localeurl import utils

register = template.Library()



def chlocale(url, locale):
    """
    Changes the URL's locale prefix if the path is not locale-independent.
    Otherwise removes locale prefix.
    """
    _, path = utils.strip_script_prefix(url)
    _, path = utils.strip_path(path)
    return utils.locale_url(path, locale)


chlocale = stringfilter(chlocale)
register.filter('chlocale', chlocale)
