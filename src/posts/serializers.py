from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from posts.models import Post

class BlogSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )

    def get_blog_url(self, instance):
        return reverse_lazy('api_post_list', kwargs={'username': instance.username})

class PostSerializer(serializers.Serializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('create_at', 'modified_at')
