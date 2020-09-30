from django.db import models
from timezone_field import TimeZoneField


# Create your models here.
class Userdetail(models.Model):
    userid = models.CharField(max_length=10)
    real_name = models.CharField(max_length=20)
    tz = TimeZoneField(default='Europe/London')



class Activity(models.Model):
    userid = models.CharField(max_length=10)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
