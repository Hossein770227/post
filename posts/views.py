from django.shortcuts import render
from django.views import generic

from .models import Post


class PostListView(generic.Listview):
    model=Post
    template_name='posts/post_list.html'
    context_objects_name='posts'