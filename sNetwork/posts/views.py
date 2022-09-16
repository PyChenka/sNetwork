from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts
        }
    return render(request, template, context)


def groups(request):
    template = 'posts/groups.html'
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'group': group
        }
    return render(request, template, context)
