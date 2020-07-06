from django import template

from ..models import Project

register = template.Library()


@register.inclusion_tag("blocks/product_tags.html", takes_context=True)
def products(context):
    return {"products": Project.objects.all(), "request": context["request"]}
