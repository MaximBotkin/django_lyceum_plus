from django.urls import path
from homepage.views import HomepageView


app_name = "homepage"


urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("tag/<str:tag_filter>/", HomepageView.as_view(), name="home_with_filter"),
]
