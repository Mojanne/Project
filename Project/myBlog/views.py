from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)


def homepage(request):
    context = {
        'postKey': Post.objects.all()
    }
    return render(request, 'myBlog/homepage.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'myBlog/homepage.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'postKey'
    ordering = ['-date']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Add author before the form is created
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Users can only update their own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # if post is successfully deleted redirect to the homepage
    success_url = '/'

    # Users can only update their own post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'myBlog/aboutpage.html', {'title': 'About'})
