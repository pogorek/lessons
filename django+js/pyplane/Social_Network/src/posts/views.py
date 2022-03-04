from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from profiles.models import Profile


# Create your views here.
def post_list_and_create(request):
    form = PostForm(request.POST or None)
    # qs = Post.objects.all()

    if request.method == 'POST':  # was is_ajax
        if form.is_valid():
            author = Profile.objects.get(user=request.user)
            # save form instance to instance, without commit
            instance = form.save(commit=False)
            # add author to form
            instance.author = author
            instance.save()

    context = {
        "form": form,
    }

    return render(request, 'posts/main.html', context)


# def load_post_data_view(request, **kwargs):
#    num_posts = kwargs.get("num_posts")

def load_post_data_view(request, num_posts):
    # how many posts will be visible
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    # old version
    # data = serializers.serialize("json", qs)
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'body': obj.body,
            # one line if-else if user liked post
            'liked': True if request.user in obj.liked.all() else False,
            'count': obj.liked_count,
            'author': obj.author.user.username
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size': size})


def like_unlike_post(request):
    # if request.is_ajax(): # doesn't work work - obsolete
    if request.method == 'POST':

        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)

    return JsonResponse({'liked': liked, 'count': obj.liked_count})