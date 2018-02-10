from django import forms
from .models import Comment,Post

class PostsForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=['title','text','image']
		widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20,'placeholder':"Title Here",'label':""}),
        	'title':forms.Textarea(attrs={'cols':80,'rows':2}),
        }

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
	