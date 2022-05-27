from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "category",
            "text",
            "tags",
        ]

    attachments = forms.ImageField(
        required=False,
        label="Изображения",
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )
