from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from description.models import Category


class CategoryPostsView(TemplateView, ContextMixin):
    template_name = 'categories/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get_category_with_posts(self.kwargs['category_id'])
        print(context['category'])
        return context
