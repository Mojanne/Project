from django.shortcuts import render
from .models import Post

def homepage(request):
    context = {
        'postKey': Post.objects.all()
    }
    return render(request, 'myBlog/homepage.html', context)

def about(request):
    return render(request, 'myBlog/aboutpage.html', {'title':'About'})


