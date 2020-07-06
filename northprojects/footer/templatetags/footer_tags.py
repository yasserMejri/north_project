from django import template
from footer.models import Footer


register = template.Library()


@register.simple_tag()
def get_footer():
    return Footer.objects.all()
