
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('account.urls')),
    path('admin/', admin.site.urls),
    path('social-auth/',include('social_django.urls')), 
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)

