#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 17:30
# @Author  : hongzai
# @Email   : 2505811377@qq.com
# @Description: 
# @File    : serializers.py
from rest_framework import serializers
from .models import ActivityPage


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPage
        # fields = "__all__"
        fields = ('activity_intro','activity_image','first_published_at','latest_revision_created_at','activity_body')

