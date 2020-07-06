from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Service(ClusterableModel):
    """The main menu clusterable model."""

    service_title = models.CharField(max_length=500, blank=True)
    service_detail = models.TextField(max_length=500, blank=True)

    service_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("service_title"),
                FieldPanel("service_detail"),
                ImageChooserPanel("service_image"),
            ],
            heading="Service",
        ),
        # InlinePanel("product_items", label="Product Item", heading="Products")
    ]

    def __str__(self):
        return self.service_title
