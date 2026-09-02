from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone 
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Category'
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        super().save(*args, **kwargs)
        
        
    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')