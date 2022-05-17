from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.base import ContextMixin
from .models import CustomUser
from .forms import RegistrationForm, Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from posts.models import Post


class UserListView(ListView):
    queryset = CustomUser.objects.get_all_active_users()
    context_object_name = 'users'
    template_name = 'users/user_list.html'


class UserDetailView(DetailView):
    model = CustomUser
    context_object_name = 'user'
    pk_url_kwarg = 'user_id'
    template_name = 'users/user_detail.html'


class SignupView(FormView):
    form_class = RegistrationForm
    success_url = '/auth/login/'
    template_name = 'users/auth/signup.html'

    def form_valid(self, form):
        form.register()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView, ContextMixin):
    template_name = 'users/profile.html'

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = Profile(request.POST or None, request.FILES or None, instance=user)
        print(dir(request))
        print(request.FILES)
        if user_form.is_valid():
            print(request.FILES)
            user_form.save()
            return redirect("/users/profile")
        else:
            return self.get(request, {'form': user_form})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['form'] = Profile(self.request.POST or None, instance=self.request.user)
        context['posts'] = Post.objects.filter(author=self.request.user)
        return context
