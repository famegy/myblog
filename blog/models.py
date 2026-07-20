from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone 
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)