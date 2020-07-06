from django.db import models
from django_extensions.db.fields import AutoSlugField
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Footer(ClusterableModel):

    title = models.CharField(max_length=500, blank=True)

    slug = AutoSlugField(populate_from="title", editable=True)

    introduction = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    email = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=500, blank=True)
    economy = models.CharField(max_length=500, blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"),
                FieldPanel("slug"),
                FieldPanel("introduction"),
                FieldPanel("address"),
                FieldPanel("email"),
                FieldPanel("phone"),
                FieldPanel("economy"),
            ],
            heading="Footer",
        )
    ]

    def __str__(self):
        return self.title
