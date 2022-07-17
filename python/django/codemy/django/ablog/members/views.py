from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from theblog.models import Profile


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    # LOGIN_REDIRECT_URL = 'home' w settings.py


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm  # UserChangeForm / przed update
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")
    # LOGIN_REDIRECT_URL = 'home' w settings.py

    # function will return current user
    def get_object(self):
        return self.request.user


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    # przesyłanie argumentow jak w funkcji {"oko": oko}
    def get_context_data(self, *args, **kwargs):
        # zapytanie o wszystkie obiekty w klassie Profile
        # users = Profile.objects.all()
        # ??
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        # ???
        # zapytanie o obiekt z id pk
        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])

        context["page_user"] = page_user
        return context


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    # fields = ["bio", "profile_pic", "website_url", "fb_url"]

    # ustawia zalogowanego uzytkownika jako autora
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ["bio", "profile_pic", "website_url", "fb_url"]
    success_url = reverse_lazy("home")


# view for success redirection after changing password, here redirection and form
class PasswordsChangeView(PasswordChangeView):
    # przed zrobieniem swojego z bootstrapem
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    # old, before we had page for success
    # success_url = reverse_lazy("home")
    success_url = reverse_lazy("password_success")


# view of successfully changing password, here is page
def password_success(request):
    return render(request, "registration/password_success.html", {})
