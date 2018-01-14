from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from posts.forms import NewPostForm
from posts.models import Post


def home (request):
    latest_posts = Post.objects.all().order_by("-publication_date")

    if len(latest_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        context = {'posts': latest_posts[:5]}
        return render(request, "home.html", context)

def blogs_list (request):

    allblogs = User.objects.all()

    if len(allblogs) == 0:
        return render(request, "404.html", status=404)
    else:
        context = {'blogs': allblogs}
        return render(request, "blogs.html", context)

def blog_detail(request,blogger):

    blog = Post.objects.filter(user=blogger)

    if len(blog) == 0:
        return render(request, "404.html", status=404)
    else:
        context = {'blog': blog}
        return render(request, "blogdetail.html", context)

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        context['username'] = user
        return context

@login_required
def post_detail(request, user, pk):
    possible_posts = Post.objects.filter(user=user, pk=pk).select_related("category")
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post = possible_posts[0]
        context = {'post': post}
        return render(request, "post_detail_page.html", context)


