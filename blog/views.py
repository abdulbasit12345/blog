from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Post


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class DetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class CreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = '__all__'

class UpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title','body']
    fields = ['title','body']


class DeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')
