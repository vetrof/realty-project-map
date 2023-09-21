from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from tbot.views import telegram_webhook, my_test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include('map.urls')),
    path('', include('realty.urls')),
    path('tbot/', telegram_webhook),
    path('tbot/test/', my_test_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



