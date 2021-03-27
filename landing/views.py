from django.shortcuts import render
import sys
from datetime import datetime
from .models import Post

# Create your views here.
def landing_view(request):

    active_posts = Post.objects.filter(is_active = True, is_publicated = True).order_by('sort_order')

    posts = {'posts': active_posts}

    for post in active_posts:
        print(post.post_title)

    return render(request, 'landing/landing.html', posts )
