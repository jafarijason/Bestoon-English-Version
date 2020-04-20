# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Expense
from .models import Income

admin.site.register(Expense)
admin.site.register(Income)


# Register your models here.
