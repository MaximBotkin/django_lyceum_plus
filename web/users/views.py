from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import FormView, TemplateView
from django.views.generic.base import ContextMixin
from posts.models import Post

from .forms import Profile, RegistrationForm
from .models import CustomUser, Subscription

User = get_user_model()


class UserListView(TemplateView):
    template_name = "users/user_list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, *args, **kwargs):
        result = []
        if "input" in request.POST and request.POST["input"]:
            result = CustomUser.objects.filter(
                username__startswith=request.POST["input"]
            )
            if not result:
                result = ["empty"]
        return render(
            request, self.template_name, context=self.get_context_data(result)
        )

    def get_context_data(self, users_to_find=[], **kwargs):
        context = super().get_context_data(**kwargs)
        users = []
        if not users_to_find:
            users_to_find = CustomUser.objects.get_all_active_users()
        elif users_to_find == ["empty"]:
            users_to_find = []
        for user in users_to_find:
            followers = len(
                Subscription.objects.filter(person=user, is_subscribed=True)
            )
            following = len(
                Subscription.objects.filter(subscriber=user, is_subscribed=True)
            )
            posts = len(Post.objects.filter(author=user))
            user_to_add = {
                "avatar": user.avatar,
                "username": user.username,
                "description": user.description,
                "followers": followers,
                "following": following,
                "posts": posts,
            }
            users.append(user_to_add)
        context["users"] = users
        return context


class UserDetailView(TemplateView):
    template_name = "users/user_detail.html"

    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(CustomUser, username=username, is_active=True)
        posts = Post.objects.filter(author=user)
        followers = Subscription.objects.filter(person=user, is_subscribed=True)
        following = Subscription.objects.filter(subscriber=user, is_subscribed=True)
        if request.user.is_authenticated:
            if_person_follows = Subscription.objects.filter(
                person=user, subscriber=request.user, is_subscribed=True
            )
        else:
            if_person_follows = False
        context = {
            "user": user,
            "posts": posts,
            "followers": followers,
            "following": following,
            "if_person_follows": if_person_follows,
        }
        return render(request, self.template_name, context)

    def post(self, request, username, *args, **kwargs):
        user = get_object_or_404(CustomUser, username=username, is_active=True)
        if "follow" in request.POST and request.POST["follow"] == "Подписаться":
            sub = Subscription(person=user, subscriber=request.user)
            sub.save()
        else:
            sub = Subscription.objects.get(person=user, subscriber=request.user)
            if sub:
                sub.delete()
        return redirect("users:user_detail", username)


class SignupView(FormView):
    form_class = RegistrationForm
    success_url = "/auth/login/"
    template_name = "users/auth/signup.html"

    def form_valid(self, form):
        form.register()
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView, ContextMixin):
    template_name = "users/profile.html"

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = Profile(request.POST or None, request.FILES or None, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect("/users/profile")
        else:
            return self.get(request, {"form": user_form})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["form"] = Profile(self.request.POST or None, instance=self.request.user)
        context["posts"] = Post.objects.filter(author=self.request.user)
        return context


def validate_username(request):
    username = request.GET.get("username", None)
    response = {
        "is_username_taken": User.objects.filter(username__iexact=username).exists(),
    }
    return JsonResponse(response)


def validate_email(request):
    email = request.GET.get("email", None)
    response = {
        "is_email_taken": User.objects.filter(email__iexact=email).exists(),
    }
    return JsonResponse(response)
