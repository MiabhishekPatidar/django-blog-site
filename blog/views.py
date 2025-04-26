from django.shortcuts import render, get_object_or_404
from .models import Post

# Home page view
def index(request):
    return render(request, 'blog/index.html')

# List all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# View post by ID
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
