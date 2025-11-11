from django.contrib import admin
from django.urls import path, include
from login.views import LoginView
from other.views import IndexView, HelloWorldView, RandomNumberView, CurrentDateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('other/', IndexView.as_view(), name='index'),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('random/', RandomNumberView.as_view(), name='random'),
    path('date/', CurrentDateView.as_view(), name='date'),
    path('store/', include(('store.urls', 'store'), namespace='store'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)