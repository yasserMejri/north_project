
# Create your models here.
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Project(ClusterableModel):
    """The main menu clusterable model."""
    product_title = models.CharField(max_length=500, blank=True)
    product_detail = models.TextField(max_length=500, blank=True)
    product_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    call_to_action = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("product_title"),
                FieldPanel("product_detail"),
                ImageChooserPanel("product_image"),
                PageChooserPanel("call_to_action"),
            ],
            heading="Projects",
        ),
        # InlinePanel("product_items", label="Product Item", heading="Products")
    ]

    def __str__(self):
        return self.product_title
