from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from django.urls import reverse
from .models import PostImage

class PostsView(TemplateView, ContextMixin):
    template_name = 'posts/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['posts'] = Post.objects.get_collection(self.request.user)
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'category',
        'text',
        'tags',
        'upload',
    ]
    template_name = 'posts/new_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:home')

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = super().get_context_data(**kwargs)
        item = self.get_object()
        context['images'] = PostImage.objects.filter(post_id=post.id)
        return context