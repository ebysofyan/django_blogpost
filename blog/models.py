from django.db import models
from django.contrib.auth.models import User
import autoslug
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None, blank=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255)
    slug = autoslug.AutoSlugField(populate_from='title')
    category = models.ForeignKey(Category, related_name='posts')
    content = RichTextUploadingField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
