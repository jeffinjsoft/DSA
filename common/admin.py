# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.



from . import models

admin.site.register(models.Ami)
admin.site.register(models.Volume)
admin.site.register(models.Vpc)
admin.site.register(models.Eip)
admin.site.register(models.Sg)
