# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Link,SideBar


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','href','status','weight','owner','created_time')
    list_filter = ("title",)


class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title','display_type','content','owner','created_time')
    list_filter = ("title",)


admin.site.register(Link,LinkAdmin)
admin.site.register(SideBar,SideBarAdmin)
