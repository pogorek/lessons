from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images', blank=True)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    # return all users who liked post
    def get_liked(self):
        return self.liked.all()

    # return number of likes
    @property
    def liked_count(self):
        return self.liked.all().count()

    # returns if user liked post
    def get_user_liked(self, user):
        pass
