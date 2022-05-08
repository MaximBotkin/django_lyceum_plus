from django.contrib import admin
from django.urls import path, include
from users.auth_urls import urlpatterns as auth_urls
from posts.urls import urlpatterns as posts_urls
from web import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include('users.urls')),
    path("auth/", include(auth_urls)),
    path("", include(posts_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
