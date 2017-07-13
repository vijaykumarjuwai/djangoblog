from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()[:5]
    context = {'posts': posts}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'detail.html', {'post': post})
