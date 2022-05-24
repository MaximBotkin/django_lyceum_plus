from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from posts.models import Post
from description.models import Category
from django.shortcuts import render
from core.views import FilterPostByTagMixin


class HomepageView(TemplateView, ContextMixin, FilterPostByTagMixin):
    template_name = "homepage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["posts"] = self.apply_filter(
            Post.objects.get_collection(self.request.user),
            self.request.GET.get("tag_filter", ""),
        )
        context["categories"] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        result = []
        if request.POST['input']:
            result = Post.objects.filter(title__contains=request.POST['input']).order_by('-creation_date')
        context['posts'] = result
        return render(request, self.template_name, context)
