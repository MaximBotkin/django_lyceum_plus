from django.http import JsonResponse
from django.views.generic import ListView, FormView, TemplateView
from django.views.generic.base import ContextMixin
from .models import CustomUser, Subscription
from .forms import RegistrationForm, Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from posts.models import Post
from django.contrib.auth import get_user_model


User = get_user_model()


class UserListView(ListView):
    queryset = CustomUser.objects.get_all_active_users()
    context_object_name = "users"
    template_name = "users/user_list.html"


class UserDetailView(TemplateView):
    template_name = "users/user_detail.html"

    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(CustomUser, username=username, is_active=True)
        posts = Post.objects.filter(author=user)
        followers = Subscription.objects.filter(person=user, is_subscribed=True)
        following = Subscription.objects.filter(subscriber=user, is_subscribed=True)
        if_person_follows = Subscription.objects.filter(
            person=user, subscriber=request.user, is_subscribed=True
        )
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
        follow = request.POST["follow"]
        if follow == "Подписаться":
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


def validate_username(req):
    username = req.GET.get("username", None)
    response = {
        "is_username_taken": User.objects.filter(username__iexact=username).exists(),
    }
    return JsonResponse(response)


def validate_email(req):
    email = req.GET.get("email", None)
    response = {
        "is_email_taken": User.objects.filter(email__iexact=email).exists(),
    }
    return JsonResponse(response)
