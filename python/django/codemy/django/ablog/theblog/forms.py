from django import forms
from .models import Post, Category, Comment

# list of tuple, "x", "x" pierwsze to nazwa, drugie the thing
# hard coded
# cat_choices = [
#     ("coding", "coding"),
#     ("sports", "sports"),
#     ("entertainment", "entertainment"),
# ]

# v2
# quert o Category model to get names
# we want to grab specific list of values from there like "x", "x"
cat_choices = Category.objects.all().values_list("name", "name")

# pusta lista dla categorii
cat_choices_list = []

# wypełniamy liste cat_choices_list tuplami
# to zwylka lista, a nie dziwny Query Set
for category in cat_choices:
    cat_choices_list.append(category)


# clasa dodajaca atrybuty do pol
class PostForm(forms.ModelForm):
    class Meta:
        # w jakim modelu ma dodac atrybuty
        model = Post
        # jakie pola maja byc w tej klasie
        fields = ("title", "title_tag", "category",
                  "header_image", "body", "snippet")

        # dodaje atrybuty do pol okreslonych w modelu
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title of Post"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            # aurhor usuniety bo w views.py funkcja dodaje aktualnie zalogowanego
            # "author": forms.Select(attrs={"class": "form-control"}),
            # choices musi byc pierwsze, choices i nazwa listy mozliwosci
            "category": forms.Select(choices=cat_choices_list, attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "snippet",)

        # dodaje atrybuty do pol okreslonych w modelu
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title goes here"}),
            # "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body",)

        # dodaje atrybuty do pol(jak css) okreslonych w modelu
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
