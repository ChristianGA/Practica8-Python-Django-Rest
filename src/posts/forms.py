from django.forms import ModelForm

from posts.models import Post


class NewPostForm(ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["user"]