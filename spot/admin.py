# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from . import models


def start(modeladmin, request, queryset):
    queryset.update(active=True)
    for i in queryset:
        print i.key
start.short_description = "Start"

def stop(modeladmin, request, queryset):
    queryset.update(active=False)
    for i in queryset:
        print i.key
stop.short_description = "Stop"

@admin.register(models.Asg)
class AsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'active','instance_type','refreshed_at')

    fieldsets = (
        ('Main', {
            'fields': ('name', 'vpc', 'sgs')
        },),
        ('Compute', {
            'fields': ('key', 'instance_type', 'instance_profile',)
        },),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('max_spot', 'eip','volumes'),
        }),
    )

    actions = [start,stop]
    # fields = ['name', 'ami']
