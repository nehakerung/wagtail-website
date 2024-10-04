from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField

from streams import blocks

# Create your models here.
class Flexpage(Page):

    template = "flex/flex_page.html"

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock())
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"