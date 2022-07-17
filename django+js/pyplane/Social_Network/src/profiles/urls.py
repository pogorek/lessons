from django.urls import path
from .views import profile_test_view, MyProfileView, MyProfileData

app_name = 'profiles'
urlpatterns = [
    path('my/', MyProfileView.as_view(), name="my-profile-view"),
    path('my-profile-json/', MyProfileData.as_view(), name="my-profile-json"),

    path('test/', profile_test_view, name="profile-test"),

    # json | endpoints
    #path('posts-json/', post_view_json, name="post-view-json"),

]
