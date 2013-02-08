# -*- coding: cp1252 -*-
from django.db import models
import datetime
from django.utils import timezone
class General(models.Model):
    code = (
        (1, "dev123"),
        (2, "sap146"),
        (3, "bd1245"),
        (4, "ads149"),
    )
    countries = (
        (1, "India"),
        (2, "UK"),
        (3, "USA"),
        (4, "Australia"),
    )
    job_code = models.IntegerField(choices=code, default=1)
    name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    country = models.IntegerField(choices=countries, default=1)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pin = models.IntegerField(max_length=20)
    phone = models.CharField(max_length=20)
    def __unicode_(self):
        return self.name
    
class Education(models.Model):
    
    general = models.ForeignKey(General)
    institution = models.CharField(max_length=50)
    boardORuniversity = models.CharField(max_length=30)
    streamORbranch = models.CharField(max_length=20)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    percentage = models.IntegerField()
