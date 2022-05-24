from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from posts.models import Post
from description.models import Category
from django.shortcuts import render


class HomepageView(TemplateView, ContextMixin):
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.get_collection(self.request.user)
        context['categories'] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        result = []
        if request.POST['input']:
            result = Post.objects.filter(title__contains=request.POST['input']).order_by('-creation_date')
        context['posts'] = result
        return render(request, self.template_name, context)
