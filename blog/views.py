from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import PostForm

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


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
        
    else:
        form = PostForm()
        
    return render(request, 'blog/post_form.html', {'form': form})