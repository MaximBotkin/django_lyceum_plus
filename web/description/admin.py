from django.contrib import admin
import description.models as models
from taggit.admin import Tag


admin.site.unregister(Tag)
admin.site.register(models.LikeDislike)
admin.site.register(models.Category)
admin.site.register(models.Tag)
