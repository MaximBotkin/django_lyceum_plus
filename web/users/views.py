from django.views.generic import ListView, DetailView, TemplateView, FormView
from .models import CustomUser
from .forms import RegistrationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class UserListView(ListView):
    queryset = CustomUser.objects.get_all_active_users()
    context_object_name = 'users'
    template_name = 'users/user_list.html'


class UserDetailView(DetailView):
    model = CustomUser
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    template_name = "users/user_detail.html"


class SignupView(FormView):
    form_class = RegistrationForm
    success_url = '/auth/login/'
    template_name = "users/auth/signup.html"

    def form_valid(self, form):
        form.register()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'users/profile.html'
