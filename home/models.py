from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel


class HomePage(Page):
    head = RichTextField(blank=True)
    body = RichTextField(blank=True)
    caption1 = RichTextField(blank=True)
    caption2 = RichTextField(blank=True)
    caption3 = RichTextField(blank=True)
    panels=[
        FieldPanel('caption1'),
        FieldPanel('caption2'),
        FieldPanel('caption3'),
        ]

    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('head', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('caption1'),
        FieldPanel('caption2'),
        FieldPanel('caption3'),
        ImageChooserPanel('icon'),
    ]
   