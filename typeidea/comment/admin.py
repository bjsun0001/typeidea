# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content','nickname','website','email','created_time')
    list_filter = ("nickname",)


admin.site.register(Comment,CommentAdmin)

