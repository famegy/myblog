from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    posts_qs = Post.objects.filter(is_published=True).order_by('-published_at')
    paginator = Paginator(posts_qs, 5) # Show 5 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'posts':posts})
  
def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug, is_published=True)
  
  return render(request, 'blog/post_detail.html', {'post': post})