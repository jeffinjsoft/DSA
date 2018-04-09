# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Ami(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='null')
    ami_id = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
       return self.ami_id

class Volume(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='null')
    vid = models.CharField(max_length=50)
    instance_id = models.CharField(max_length=50,default='null')
    a_zone = models.CharField(max_length=50,default='null')
    snap_id = models.CharField(max_length=50,default='null')
    state = models.CharField(max_length=50,default='available')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.vid

    def fullname(self):
        return str(self.vid)+' | '+str(self.name)[:10]

class Keypair(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


    def __unicode__(self):
       return self.name

class Vpc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='null')
    vpc_id = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
       return self.vpc_id


class InstanceProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    arn = models.CharField(max_length=50)


    def __unicode__(self):
       return self.name

class InstanceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


    def __unicode__(self):
       return self.name

class Eip(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='null')
    eip = models.CharField(max_length=50)
    allow_id = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
       return self.eip

class Sg(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='null')
    sg_id = models.CharField(max_length=50)
    vpc = models.ForeignKey(Vpc,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
       return self.sg_id
