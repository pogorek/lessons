from django.db import models
from django.contrib.auth.models import User
from itertools import chain
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatar.jpg')
    background = models.ImageField(
        upload_to='backgrounds', default='background.jpg')
    following = models.ManyToManyField(
        User, related_name='following', blank=True)
    bio = models.TextField(default="no bio...")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of the user {self.user.username}"

    # get all Profile/User posts | reverse relationship Profile > Post
    def get_my_posts(self):
        return self.post_set.all()

    # get number of my posts | property makes it will be treated as a field
    @property
    def num_posts(self):
        return self.post_set.all().count()

    # get queryset of following users
    def get_following(self):
        return self.following.all()

    # get list of following users
    def get_following_users(self):
        following_list = [p for p in self.get_following()]
        return following_list

    # get count of following users
    @property
    def following_count(self):
        return self.get_following().count()

    # get posts of following users and my posts
    def get_my_and_following_posts(self):
        '''
        1) get the list of users that are following us
        2) initialize an empty posts list and set qs equal to none
        3) loop through the users list
        3A) for each user that we are following - grab it's profile
        3B) for every profile that we know have - grab the posts
        3C) add the posts to the post list
        4) grab our posts
        5) if posts list isn't empty sort the posts by created date
        '''
        users = [user for user in self.get_following()]
        posts = []
        qs = None
        for u in users:
            p = Profile.objects.get(user=u)
            p_posts = p.post_set.all()
            posts.append(p_posts)
        my_posts = self.post_set.all()
        posts.append(my_posts)
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True,
                        key=lambda obj: obj.created)
        return qs

    # get 3 proposals of users that we not following
    def get_proposals_for_following(self):
        '''
        1) get the profiles excluding our own
        2) create the followers list for our profile
        3) create and available list where:
            - we loop through the profiles
            - next we check if a particular profile is not on the followers list
            - only then we add that profile to the available list
        4) we shuffle the available list
        5) we return 3 first items of the available list
        '''
        profiles = Profile.objects.all().exclude(user=self.user)
        followers_list = [p for p in self.get_following()]
        available = [p.user for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]

    # get all users following me
    def get_followers(self):
        '''
        1) Create a queryset of all profiles
        2) create an empty followers list
        3) loop through the profiles
        4) perform and if statement to check if a single profile has us on the following list
        5) if the if check is true - add this profile to the followers list
        '''
        qs = Profile.objects.all()
        followers_list = []
        for profile in qs:
            if self.user in profile.get_following():
                followers_list.append(profile)
        return followers_list

    # get count of all users following me
    @property
    def followers_count(self):
        return len(self.get_followers())
