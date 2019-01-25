from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=15, verbose_name="标题")
    content = models.TextField(max_length=500, null=True, blank=True, verbose_name="内容")

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=15, verbose_name="姓名")
    # content = models.TextField(max_length=500, null=True, blank=True, verbose_name="内容")

    def __str__(self):
        return self.name