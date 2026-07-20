from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(is_published=True)
    
    return render(request, 'blog/post_list.html', {'posts':posts})
  
def post_detail(request, slug):
  post = 