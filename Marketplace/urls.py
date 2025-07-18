from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('conversation/', include('conversation.urls', namespace='conversation')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
