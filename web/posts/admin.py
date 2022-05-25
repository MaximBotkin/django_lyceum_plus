from django.contrib import admin

from .models import Post, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title")
    list_display_links = ("title",)
    inlines = [PostImageAdmin]

    class Meta:
        model = Post

    def view_on_site(self, obj):
        return obj.get_absolute_url()


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
