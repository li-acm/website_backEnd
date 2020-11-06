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

class ActivityPage(Page):
    activity_intro = models.CharField(max_length=255, help_text="活动介绍", verbose_name='活动介绍')
    activity_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='首页图',
        verbose_name='首页图'
    )
    activity_created_at = models.DateField(auto_now_add=True)
    activity_body = StreamField([

        ('文章', blocks.RichTextBlock()),
        ('图片', ImageChooserBlock(icon="image")),
    ],null=True,blank=True,help_text='内容',verbose_name='内容')

    content_panels = Page.content_panels + [
        FieldPanel('activity_intro'),
        ImageChooserPanel('activity_image'),
        StreamFieldPanel('activity_body'),
    ]

    # Export fields over the API
    api_fields = [
        APIField('activity_intro'),
        APIField('activity_image'),
        APIField('activity_image_thumbnail', serializer=ImageRenditionField('fill-300x186', source='activity_image')),
        APIField('activity_body'),
        APIField('activity_created_at', serializer=DateField(format='%A %d %B %Y')),
        # APIField('published_date', serializer=DateField(format='%A %d %B %Y')),
         # Date in ISO8601 format (the default)
    ]

class IndexActivityPage(Page):
    activity_intro = models.CharField(max_length=255, help_text="活动页", verbose_name='活动页')


    content_panels = Page.content_panels + [
        FieldPanel('activity_intro'),
    ]

class RootPage(Page):
    root_intro = models.CharField(max_length=255, help_text="根页面", verbose_name='根页面')
    content_panels = Page.content_panels + [
        FieldPanel('root_intro'),
    ]