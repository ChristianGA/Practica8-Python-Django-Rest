from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from posts.forms import NewPostForm
from posts.models import Post


class HomeView(ListView):
    model = Post
    template_name = "home.html"

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset.order_by("-publication_date")

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail_page.html"

    def get_queryset(self):
        autor = self.kwargs.get('username')
        pk = self.kwargs.get('pk')
        queryset = Post.objects.filter(user__username=autor, pk=pk)
        return queryset

class BlogsListView(ListView):
    model = User
    template_name = "blogs.html"

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

class NewPostView(LoginRequiredMixin, View):

    def get(self, request):
        form = NewPostForm()
        return render(request, "newpost_form.html", {'form': form})

    def post(self, request):
        post = Post()
        post.user = request.user
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            form = NewPostForm()
            url = reverse("post_detail_page", args=[post.pk])
            message = "Post created successfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)
        return render(request, "newpost_form.html", {'form': form})

class MyPostsView(ListView):

    model = Post
    template_name = "myposts.html"

    def get_queryset(self):
        queryset = super(MyPostsView, self).get_queryset()
        username = self.kwargs.get('username')
        return queryset.filter(user__username=username).order_by('-publication_date')

    def get_context_data(self, *args, **kwargs): #función para meter info del usuario de la URL blogs/username
        context = super().get_context_data(*args, **kwargs)
        autor = self.kwargs.get('username')
        user = get_object_or_404(User, username=autor)
        context['autor'] = user
        return context


