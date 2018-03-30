# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category,Tag,Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','is_nav','status','owner','created_time')
    list_filter = ("name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name','status','owner','created_time')
    list_filter = ("name",)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','status','owner','created_time')
    list_filter = ('category',)
    search_fields = ("title","category__name","owner__username",)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)
