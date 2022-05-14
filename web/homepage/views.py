from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from posts.models import Post
from description.models import Category


class HomepageView(TemplateView, ContextMixin):
    template_name = 'homepage/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.get_collection(self.request.user)
        context['categories'] = Category.objects.all()
        return context
