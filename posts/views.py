from django.shortcuts import render
from .models import Post
from .models import Image
# Create your views here.

def index(request):
    posts = Post.objects.all()
    pics=Image.objects.all()
    return render(request, 'index.html',{'posts': posts, 'pics': pics})

def post(request,pk):
    posts = Post.objects.get(id = pk)
    return render(request, 'post.html', {'posts': posts})
