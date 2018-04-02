# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db import connection

from .models import Post,Tag,Category
from config.models import SideBar
from comment.models import Comment


def get_common_context():
    categories = Category.objects.filter(status=1)

    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    side_bars = SideBar.objects.filter(status=1)

    recently_posts = Post.objects.filter(status=1)[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]
    
    context = {
        'nav_cates': nav_cates,
        'cates': cates,
        'side_bars': side_bars,
        'recently_posts': recently_posts,
        'recently_comments': recently_comments,
    }
    return context



def post_list(request,category_id=None,tag_id=None):
    queryset = Post.objects.all()
    if category_id:
        #分类页面
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        #标签页面
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset =tag.posts.all()
     
    paginator = Paginator(queryset,2)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        queryset_list = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        queryset_list = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        queryset_list = current_page.object_list

 
    
    #print('---------------------------------------------')

    #print(connection.queries)


    context = {
        'posts': queryset_list,
        'page': current_page,
    }
    common_context = get_common_context()
    context.update(common_context)
    return render(request,'blog/list.html',context=context)



def post_detail(request,post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = []

    context = {
        'post': post
    }
    common_context = get_common_context()
    context.update(common_context)
    return render(request,'blog/detail.html',context=context)
