from django.contrib import admin
from django.urls import path, include
from users.auth_urls import urlpatterns as auth_urls
from web import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("auth/", include(auth_urls)),
    path("", include("posts.urls", namespace="posts")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "web.views.page_not_found_view"
handler500 = "web.views.server_error"

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
