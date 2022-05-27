from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from django.urls import reverse
from .models import PostImage
from posts.forms import PostForm


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/new_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()
        for item in self.request.FILES.getlist("attachments"):
            PostImage.objects.create(image=item, post=post)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("homepage:home")


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = super().get_context_data(**kwargs)
        context["images"] = PostImage.objects.filter(post_id=post.id)
        return context
