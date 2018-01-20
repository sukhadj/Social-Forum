from django import forms
from .models import Comment,Post

class PostsForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','text','image']

		def __init__(self):
			self.fields['image'].required=False

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['comment_text']

# class PostCreateForm(forms.Form):
# 	title	=forms.CharField(max_length=200)
# 	text	=forms.TextField()
# 	image	=forms.ImageField(required=False)
	