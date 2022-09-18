import datetime
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')
    context = {
        'posts': posts
        }
    return render(request, template, context)

# def index(request):
#     author = User.objects.get(username='leo')
#     keyword = "утро"
#     start_date = datetime.datetime(1854, 7, 7, 0, 0, tzinfo=datetime.timezone.utc)
#     end_date = datetime.datetime(1854, 7, 21, 0, 0, tzinfo=datetime.timezone.utc)
#     posts = Post.objects.filter(text__contains=keyword).filter(author=author).filter(pub_date__range=(start_date, end_date))
#     return render(request, 'posts/index.html', {'posts': posts})

# def index(request):
#     keyword = request.GET.get('q', None)
#     if keyword:
#         posts = Post.objects.select_related('author', 'group').filter(text__contains=keyword)
#     else:
#         posts = None
#     return render(request, 'posts/index.html', {'posts': posts, 'keyword': keyword})


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
