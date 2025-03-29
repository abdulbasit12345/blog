from django.urls import path
from .views import BlogListView, DetailView, CreateView,UpdateView,DeleteView

urlpatterns = [
    path("post/<int:pk>/delete", DeleteView.as_view(), name="post_delete"),  # Add this line to your urls.py file.
    path("post/<int:pk>/edit", UpdateView.as_view(), name="post_edit"),  # Add this line to your urls.py file.
    path("post/new", CreateView.as_view(), name="post_new"),  # Add this line to your urls.py file.
    path("<int:pk>", DetailView.as_view(), name="post_detail"),  # Add this line to your urls.py file.
    path("", BlogListView.as_view(), name="home"),
]