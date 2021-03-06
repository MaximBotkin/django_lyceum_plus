from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users.auth_urls import urlpatterns as auth_urls

from django.views.static import serve
from django.conf.urls import url

from web import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("auth/", include(auth_urls)),
    path("posts/", include("posts.urls", namespace="posts")),
    path("", include("homepage.urls", namespace="homepage")),
    path("category/", include("description.categories_urls", namespace="category")),
    path("comments/", include("django_comments.urls")),
    path("captcha/", include("captcha.urls")),
    path("", include("description.urls")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "web.views.page_not_found_view"
handler500 = "web.views.server_error"

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
