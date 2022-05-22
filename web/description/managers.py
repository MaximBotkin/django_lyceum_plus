from django.db import models


class CategoryManager(models.Manager):
    def get_category_with_posts(self, pk):
        return self.get_queryset().prefetch_related("posts").get(pk=pk)


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)
