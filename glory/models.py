from django.db import models

# Create your models here.
from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from rest_framework.fields import DateField

class gloryPage(Page):
    glory_intro = models.CharField(max_length=255, help_text="荣誉介绍", verbose_name='荣誉介绍')
    glory_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='首页图',
        verbose_name='首页图'
    )
    glory_body = StreamField([

        ('文章', blocks.RichTextBlock()),
        ('图片', ImageChooserBlock(icon="image")),
    ],null=True,blank=True,help_text='内容',verbose_name='内容')
    glory_created_at = models.DateField(auto_now_add=True)
    content_panels = Page.content_panels + [
        FieldPanel('glory_intro'),
        ImageChooserPanel('glory_image'),
        StreamFieldPanel('glory_body'),
    ]

    # Export fields over the API
    api_fields = [
        APIField('glory_intro'),
        APIField('glory_image'),
        APIField('glory_image_thumbnail', serializer=ImageRenditionField('fill-309x528', source='glory_image')),
        APIField('glory_body'),
        APIField('glory_created_at', serializer=DateField(format='%A %d %B %Y')),
        # APIField('published_date', serializer=DateField(format='%A %d %B %Y')),
         # Date in ISO8601 format (the default)
    ]

class IndexGloryPage(Page):
    glory_intro = models.CharField(max_length=255, help_text="荣誉页", verbose_name='荣誉页')


    content_panels = Page.content_panels + [
        FieldPanel('glory_intro'),
    ]

