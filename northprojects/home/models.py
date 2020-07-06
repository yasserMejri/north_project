from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from django.db import models

from home.blocks import (
    Hero_1,
    TwoCol_2,
    ImgText_3,
    ImgOnText_4,
    Featured_5,
    Staff_6,
    CImgText_8,
    DoubleImgText_10,
    ImgColorText_9,
    Services_11,
    USP_12,
)


class StandardPage(Page):
    theme_choices = (
        ('white', 'White'),
        ('black', 'Black')
    )
    theme = models.CharField(max_length=250, choices = theme_choices, default='white')
    # theme = models.CharField(max_length = 9)
    body = StreamField(
        [
            ("Hero", Hero_1()),
            ("TwoCol_2", TwoCol_2()),
            ("ImgText_3", ImgText_3()),
            ("ImgOnText_4", ImgOnText_4()),
            ("Featured_5", Featured_5()),
            ("Staff_6", Staff_6()),
            ("CImgText_8", CImgText_8()),
            ("ImgColorText_9", ImgColorText_9()),
            ("DoubleImgText_10", DoubleImgText_10()),
            ("Services_11", Services_11()),
            ("USP_12", USP_12()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('theme'),
        StreamFieldPanel("body")
    ]
