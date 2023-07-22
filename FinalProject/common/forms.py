from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django import forms

from FinalProject.common.models import Post, Comment


class SharePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'image_url', 'post_information']


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


