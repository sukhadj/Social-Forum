from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,View
from .models import Profile

User=get_user_model()


class ProfileFollowToggle(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
		user_to_toggle=request.POST.get("username")
		profile_=Profile.objects.get(user__username__iexact=user_to_toggle)
		user=request.user
		if user in profile_.followers.all():
			profile_.followers.remove(user)
		else:
			profile_.followers.add(user)
		return redirect('/profiles/{user_to_toggle.username}/')


class ProfileDetailView(DetailView):
	template_name='profiles/user_detail.html'

	def get_object(self):
		username=self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User,username__iexact=username,is_active=True)	

	def get_context_data(self,*args,**kwargs):
		context=super(ProfileDetailView,self).get_context_data(*args,**kwargs)
		user=context['user']
		is_following=False
		if user.profile in self.request.user.is_following.all():
			is_following=True
			context['is_following']=is_following
		return context 