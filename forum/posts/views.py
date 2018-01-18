from django.views.generic import DetailView,ListView,TemplateView,CreateView
from django.shortcuts import render,get_object_or_404 
from .models import Post
from .forms import PostsForm

class HomeView(TemplateView):
	template_name="home.html"
	

class PostListView(ListView):
	template_name="posts/post_list.html"
	def get_queryset(self):
		return Post.objects.all()

class PostDetailView(DetailView):
	queryset=Post.objects.all()
	template_name="posts/post_detail.html"

class PostCreateView(CreateView):
	template_name="posts/post_create.html"
	form_class=PostsForm
	