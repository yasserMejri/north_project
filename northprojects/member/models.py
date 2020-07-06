from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Member(ClusterableModel):
    name = models.CharField(max_length=500, blank=True)
    position = models.CharField(max_length=500, blank=True)
    avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [
        MultiFieldPanel(
            [FieldPanel("name"), FieldPanel("position"), ImageChooserPanel("avatar")],
            heading="Staff",
        )
    ]

    def __str__(self):
        return self.name
