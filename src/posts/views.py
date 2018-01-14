from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def home (request):
    latest_posts = Post.objects.all().order_by("-publication_date")

    if len(latest_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        context = {'posts': latest_posts[:5]}
        return render(request, "home.html", context)

def blogs_list (request):

    allblogs = Post.objects.all()

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

def post_detail (request, pk):

    return HttpResponse("Es la vista detalle!")

def login (request):

    return HttpResponse("Es la vista login!")

def logout(request):

    return HttpResponse("Es la vista logout!")

def signup(request):

    return HttpResponse("Es la vista sign up!")

def newpost(request):

    return HttpResponse("Es la vista new post!")
