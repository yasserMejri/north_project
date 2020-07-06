from django import template

from ..models import Service

register = template.Library()


@register.inclusion_tag("blocks/service_tags.html", takes_context=True)
def services(context):
    return {"services": Service.objects.all(), "request": context["request"]}
