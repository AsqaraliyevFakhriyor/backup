from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.


"""
blog get view
"""
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'



"""
blog get view detail
"""
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"



"""
blog create view
"""
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = [
        'title', 'author', 'body'
    ]

"""
blog update view
"""
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = [
        'title', 'body'
    ]


"""
blog delete view
"""
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")