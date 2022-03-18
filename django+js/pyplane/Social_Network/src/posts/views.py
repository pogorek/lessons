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

            return JsonResponse({
                "title": instance.title,
                "body": instance.body,
                "author": instance.author.user.username,
                "id": instance.id
            })

    context = {
        "form": form,
    }

    return render(request, 'posts/main.html', context)


def post_detail(request, pk):
    obj = Post.objects.get(pk=pk)
    form = PostForm()

    context = {
        'obj': obj,
        'form': form,
    }
    return render(request, 'posts/detail.html', context)


def post_detail_data_view(request, pk):
    obj = Post.objects.get(pk=pk)
    data = {
        'id': obj.id,
        'title': obj.title,
        'body': obj.body,
        'author': obj.author.user.username,
        # 'avatar': obj.author.avatar.url,
        'logged_in': request.user.username,
    }
    return JsonResponse({'data': data})


# def load_post_data_view(request, **kwargs):
#    num_posts = kwargs.get("num_posts")
def load_post_data_view(request, num_posts):
    if request.method == 'GET':  # was is_ajax
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


def update_post(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.method == 'POST':  # was is_ajax
        new_title = request.POST.get('title')
        new_body = request.POST.get('body')
        obj.title = new_title
        obj.body = new_body
        obj.save()
        return JsonResponse({
            'title': new_title,
            'body': new_body,
        })
    # return redirect('posts:main-board')


def delete_post(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.method == 'POST':  # was is_ajax
        obj.delete()
        return JsonResponse({})
        # return JsonResponse({'msg':'some message'})
    # return redirect('posts:main-board')
