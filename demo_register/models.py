from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    mobile = models.CharField(max_length=11,null=True,blank=True)
    width = models.FloatField()
    height = models.IntegerField()
    image = models.ImageField(upload_to='image/%Y/%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class Image(models.Model):
    image = models.ImageField(upload_to='image/', default='image/default.png', max_length=100)