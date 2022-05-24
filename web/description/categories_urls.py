from django.urls import path
from description.views import CategoryPostsView


app_name = "categories"


urlpatterns = [path("<int:category_id>/", CategoryPostsView.as_view(), name="category")]
