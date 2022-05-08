from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from posts.models import Post


class PostsView(TemplateView, ContextMixin):
    template_name = 'posts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.get_collection(self.request.user)
        return context
