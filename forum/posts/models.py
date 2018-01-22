from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator

User=settings.AUTH_USER_MODEL

class Post(models.Model):
	title		=models.CharField(max_length=200)
	text		=models.TextField()
	user 		=models.ForeignKey(User,default=1)
	image		=models.ImageField(blank=True,null=True,upload_to="image/Post")
	upvotes		=models.IntegerField(default=0)
	slug		=models.SlugField(null=True,blank=True)
	timestamp	=models.DateTimeField(auto_now_add=True)
	updated		=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def upvoted(self):
		self.upvotes=self.upvotes+1

	def get_absolute_url(self):
		return reverse("posts:details",kwargs={'slug':self.slug})


class Comment(models.Model):
	user 	 		=models.ForeignKey(User,default=1)
	post 			=models.ForeignKey(Post,default=1)
	comment_text 	=models.CharField(max_length=120,null=True,blank=True)
	timestamp		=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment_text

	def	get_absolute_url(self):
		return reverse("posts:details",kwargs={'slug':self.post.slug})


		

def post_pre_save(sender,instance,*args,**kwargs):
	instance.title=instance.title.capitalize()
	instance.slug=unique_slug_generator(instance) 

pre_save.connect(post_pre_save,sender=Post)