# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Q,F,Count,Sum
from django.test import TestCase
from django.test.utils import override_settings

from .models import Category


class TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user('bjsun0001','bjsun0001@163.com','password')
        for i in range(10):
            category_name = 'cate_%s' % i
            Category.objects.create(name=category_name,owner=user)
 
    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.all().prefetch_related('owner')
        print(categories.query)

        category = Category.objects.filter(id=1)

        users = User.objects.filter(username='the5ire').annotate(cate_count=Count('category'))
        #user = users[0]
        print(users.query)
 
        #print(user.cate_count)
        #categories = categories.filter(status=1)
        #print(categories.query)
        #print(list(categories))
        print('------------------------------------')
        print(connection.queries)
