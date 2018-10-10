from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostsForm, CommentForm


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated():
            return render(request, "home.html", {})
        else:

            is_following_user_ids = [x.user.id for x in user.is_following.all()]
            qs = Post.objects.filter(user__id__in=is_following_user_ids).order_by("-updated")
            return render(request, "home.html", {'object_list': qs})


class PostSelfListView(LoginRequiredMixin, ListView):
    template_name = "posts/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/post_create.html"
    form_class = PostsForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostDetailCommentView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_detail.html'
    form_class = CommentForm

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailCommentView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get("slug")
        obj = Post.objects.get(slug=slug)
        context['object'] = obj
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        slug = self.kwargs.get("slug")
        obj = Post.objects.get(slug=slug)
        instance.post = obj
        return super(PostDetailCommentView, self).form_valid(form)

# def model_form_upload(request):
# 	template_name="posts/post_create.html"
# 	if request.method=="POST":
# 		form=PostsForm(request.POST,request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('home')
# 		else:
# 			form=PostsForm()
# 		return render(request,template_name,{'form':form})
