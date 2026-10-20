from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def register(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
          user = form.save()
          login(request, user)
          return redirect('post_list')
   else:
      form = UserCreationForm()
    
   return render(request, 'accounts/register.html', {'form': form})

def author_detail(request, username):
   author = get_list_or_404(User, username=username)
   profile, _ = Profile.objects.get_or_create(user=author)
   posts = Post.objects.filter(author=author, is_publlished=True).order_by('-published_at')
   return render(request, 'accounts/author_detail.html', {
      'author': author,
      'profile': profile,
      'posts':posts,
   })


@login_required
def profile_edit(request):
   profile, _ = Profile.objects.get_or_create(user=request.user)
   
   if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES, instance=profile)
      
      if form.is_valid():
         form.save()
         return redirect ('author_details', username=request.user.username)
      
   else:
      form = ProfileForm(instance=profile)
         
   return render(request, 'accounts/profile_edit.html', {'form':form})   
      