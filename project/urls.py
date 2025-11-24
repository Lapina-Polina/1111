from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('other/', include('apps.common.urls')),
    path('other/', include('apps.test_app.urls')),
    path('other/', include('apps.login.urls')),
    path('other/cart/', include('apps.cart.urls')),
    path('', include('apps.home.urls', namespace='home')),
    path('shop/', include('apps.shop.urls')),
    path('cart_shop/', include('apps.cart_shop.urls')),
    path('checkout/', include('apps.checkout.urls')),
    path('blog/', include('apps.blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)