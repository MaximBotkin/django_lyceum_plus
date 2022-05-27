from description.views import CategoryPostsView
from django.urls import path

app_name = "categories"


urlpatterns = [path("<int:category_id>/", CategoryPostsView.as_view(), name="category")]
