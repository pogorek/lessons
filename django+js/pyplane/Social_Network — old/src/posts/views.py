from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import Post


# Create your views here.
# def home_view(request):
def post_list_and_create(request):
    qs = Post.objects.all()

    return render(request, 'posts/main.html', {
        'qs': qs,
    })


def load_post_data_view(request):

    # def post_view_json(request):
    #     qs = Post.objects.all()
    #     data = serializers.serialize("json", qs)
    #     return JsonResponse({'data': data})
