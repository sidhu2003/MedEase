from django.db import models
from django_redis import get_redis_connection
from django.core.cache import cache
# Create your models here.
class Reports(models.Model):
    s_no = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    doctor = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.s_no