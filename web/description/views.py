from django.views.generic import TemplateView
from django.views import View
from django.views.generic.base import ContextMixin
from description.models import Category
from description.models import LikeDislike
from django.contrib.contenttypes.models import ContentType
import json
from django.http import HttpResponse


class CategoryPostsView(TemplateView, ContextMixin):
    template_name = "categories/category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get_category_with_posts(
            self.kwargs["category_id"]
        )
        return context


class VotesView(View):
    model = None  # Модель данных - Статьи или Комментарии
    vote_type = None  # Тип комментария Like/Dislike

    def post(self, request):
        pk = int(request.POST.get("pk"))
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(
                content_type=ContentType.objects.get_for_model(obj),
                object_id=obj.id,
                user=request.user,
            )
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=["vote"])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True
        return HttpResponse(
            json.dumps(
                {
                    "result": result,
                    "like_count": obj.votes.likes().count(),
                    "dislike_count": obj.votes.dislikes().count(),
                }
            ),
            content_type="application/json",
        )


class CheckEstimatedView(View):
    model = None

    def get(self, req):
        pks = map(int, req.GET.getlist("pks[]"))
        result = dict()
        for pk in pks:
            obj = self.model.objects.get(pk=pk)
            result[pk] = 0
            if req.user.is_authenticated:
                try:
                    result[pk] = LikeDislike.objects.get(
                        content_type=ContentType.objects.get_for_model(obj),
                        object_id=obj.id,
                        user=req.user,
                    ).vote
                except LikeDislike.DoesNotExist:
                    result[pk] = 0
        return HttpResponse(
            json.dumps({"result": result}), content_type="application/json"
        )
