from django.db import models

# Create your models here.
from wagtail.core.models import Page

class BlogPage(Page):
    blog_title = models.CharField(max_length=400,help_text='博客名称',verbose_name='博客名称')
    blog_intro = models.CharField(max_length=400,help_text='博客概要',verbose_name='博客概要')

    class Meta:
        pass