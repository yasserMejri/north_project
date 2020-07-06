from django import template

from ..models import Member

register = template.Library()


@register.inclusion_tag("blocks/member_tags.html", takes_context=True)
def members(context):
    return {"members": Member.objects.all(), "request": context["request"]}
