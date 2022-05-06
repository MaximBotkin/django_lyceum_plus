from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    list_display_links = ('title', )
    filter_horizontal = ('tags', )
