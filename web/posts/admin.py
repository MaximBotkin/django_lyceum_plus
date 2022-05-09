from django.contrib import admin

from .models import Post, PostComment, UserComment, ReplyComment, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "image_tmb")
    list_display_links = ("title",)
    filter_horizontal = ("tags",)
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


admin.site.register(PostComment)
admin.site.register(UserComment)
admin.site.register(ReplyComment)

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass