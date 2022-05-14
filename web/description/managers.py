from django.db import models


class CategoryManager(models.Manager):
    def get_category_with_posts(self, pk):
        return self.get_queryset().prefetch_related('posts').get(pk=pk)
