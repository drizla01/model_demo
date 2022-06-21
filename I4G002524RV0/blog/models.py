import imp
from statistics import mode
from django.db import models
from django.contrib.auth.models import get_user_model
from matplotlib.pyplot import title

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)
