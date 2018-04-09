# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


from common.models import Ami,Vpc,Sg,Eip,Volume,InstanceProfile,InstanceType,Keypair

class Asg(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    ami = models.ForeignKey(Ami,on_delete=models.CASCADE)
    sgs = models.ManyToManyField(Sg)
    vpc = models.ForeignKey(Vpc,on_delete=models.CASCADE)
    key = models.ForeignKey(Keypair)
    eip = models.ForeignKey(Eip)
    volumes = models.ForeignKey(Volume,blank=True)
    instance_profile = models.ForeignKey(InstanceProfile)
    instance_type = models.ForeignKey(InstanceType)
    max_spot = models.FloatField(null=True, blank=True, default=0.05)

    ip_opt = models.CharField(max_length=5,choices=(
                                                    ('yes','yes'),
                                                    ('no','no'),
                                                    ('subnet','subnet settings'),
                                                    ))

    active = models.BooleanField(default=False)

    refreshed_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.name
