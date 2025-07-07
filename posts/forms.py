from django import forms

from posts.models import Post, PostImage


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
        widgets ={
            'title': forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control',
                'cols' : '30',
                'rows' : '10',
            })
        }
        labels = {
            'title': 'Title',
            'description': 'Description'
        }
