from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User


def index(request):
    keyword = request.GET.get('q', None)
    template = 'posts/index.html'
    if keyword:
        posts = Post.objects.select_related('author', 'group').filter(text__contains=keyword)
        context = {
            'posts': posts,
            'keyword': keyword
            }
    else:
        posts = Post.objects.order_by('-pub_date')
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
