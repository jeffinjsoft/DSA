# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from . import models






@admin.register(models.Asg)
class AsgAdmin(admin.ModelAdmin):
    # items display in main
    list_display = ('name', 'active','instance_type','refreshed_at')

    # field set in add option
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


    ## additional admin actions

    def start(self, request, queryset):
         rows = queryset.update(active=True)
         if rows == 1:
                message_bit = "1 story was"
         else:
            message_bit = "%s stories were" % rows_updated
         self.message_user(request, "%s successfully marked as published." % message_bit)

    start.short_description = "Start"


    def stop(self, request, queryset):
        rows = queryset.update(active=False)
        if rows == 1:
               message_bit = "1 story was"
        else:
           message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    stop.short_description = "Stop"

    # admin action register
    actions = [start,stop]
    # fields = ['name', 'ami']
