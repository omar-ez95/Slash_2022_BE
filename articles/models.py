from pydoc import describe
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from PIL import Image


# Create your models here.
class Article(models.Model):

    name = models.CharField(max_length=50, null=True, blank=True)
    describtion = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Discource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    describtion = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


