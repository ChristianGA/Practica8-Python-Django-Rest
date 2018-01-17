from django.contrib.auth.models import User
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView

from posts.serializers import BlogSerializer, PostSerializer


class BlogsListAPI(ListAPIView):

    serializer_class = BlogSerializer
    queryset = User.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['username']
    search_fields = ['first_name']

class PostListAPI(ListAPIView):

    serializer_class = PostSerializer
