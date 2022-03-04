from django.urls import path
from .views import (
    post_list_and_create,
    # home_view,
    post_view_json,
)

app_name = 'posts'
urlpatterns = [
    path('', post_list_and_create, name="main-board"),

    # json | endpoints
    path('posts-json/', post_view_json, name="post-view-json"),

]
