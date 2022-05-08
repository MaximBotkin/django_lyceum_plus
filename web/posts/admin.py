from django.contrib import admin

from .models import Post, PostComment, UserComment, ReplyComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title")
    list_display_links = ("title",)
    filter_horizontal = ("tags",)


admin.site.register(PostComment)
admin.site.register(UserComment)
admin.site.register(ReplyComment)
