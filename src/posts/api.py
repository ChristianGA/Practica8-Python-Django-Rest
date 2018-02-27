from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.permissions import UserpostPermission
from posts.serializers import BlogSerializer, PostSerializer

class AdminOwnerFuturePost:

    def get_queryset(self):
        autor = self.kwargs.get('username')
        queryset = Post.objects.filter(user__username=autor)
        user = self.request.user
        if user.is_authenticated != autor and not user.is_superuser:
            queryset = queryset.filter(publication_date__lte = datetime.now())
        return queryset


class BlogsListAPI(ListAPIView):

    serializer_class = BlogSerializer
    queryset = User.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['username']
    search_fields = ['first_name']

class PostListAPI(AdminOwnerFuturePost, ListAPIView):

    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'summary', 'body')
    ordering_fields = ('title', 'publication_date')
    ordering = ('-publication_date')

class PostCreateAPI(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailUpdateDeleteAPI(AdminOwnerFuturePost, RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [UserpostPermission]
