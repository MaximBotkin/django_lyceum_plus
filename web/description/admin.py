import description.models as models
from django.contrib import admin
from taggit.admin import Tag

admin.site.unregister(Tag)
admin.site.register(models.LikeDislike)
admin.site.register(models.Category)
admin.site.register(models.Tag)
