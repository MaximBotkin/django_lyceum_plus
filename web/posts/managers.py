from django.db import models


class PostManager(models.Manager):
    # Возвращаем подборку публикаций для пользователя
    def get_collection(self, user):
        posts = (
            self.all()
            .order_by("creation_date")
            .select_related("category", "author")
            .prefetch_related("tags")
        )
        return posts
