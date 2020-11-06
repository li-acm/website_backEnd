#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 19:52
# @Author  : hongzai
# @Email   : 2505811377@qq.com
# @Description: 
# @File    : serializers.py.py

from rest_framework import serializers
from .models import gloryPage


class GlorySerializer(serializers.ModelSerializer):
    class Meta:
        model = gloryPage
        # fields = "__all__"
        fields = ('glory_intro','glory_image','first_published_at','latest_revision_created_at','glory_body')
