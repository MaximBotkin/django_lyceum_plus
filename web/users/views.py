from django.views.generic import ListView, DetailView, TemplateView
from .models import CustomUser


class UserListView(ListView):
    queryset = CustomUser.objects.get_all_active_users()
    context_object_name = 'users'
    template_name = 'users/user_list.html'


class UserDetailView(DetailView):
    model = CustomUser
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    template_name = "users/user_detail.html"


class SignupView(TemplateView):
    template_name = 'users/auth/signup.html'
