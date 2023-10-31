from django.shortcuts import render
from django.views import generic
from .forms import PostForm
from django.urls import reverse_lazy

from .models import Post


class PostListView(generic.ListView):
    model=Post
    template_name='posts/post_list.html'
    context_object_name='posts'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('date_time_created')
    

class PostDetailView(generic.DetailView):
    model=Post
    template_name='posts/post_detail.html'
    context_object_name='post'

class PostCreateView(generic.CreateView):
    model = Post
    form_class =PostForm
    template_name = "posts/post_create.html"

    
class PostUpdateView(generic.UpdateView):
    model=Post
    form_class=PostForm
    template_name='posts/post_create.html'

class PostDeleteView(generic.DeleteView):
    model=Post
    template_name='posts/post_delete.html'
    success_url=reverse_lazy('post_list')