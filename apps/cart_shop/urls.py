from .views import ViewCartBuy, ViewCartAdd, ViewCartDel, ViewCart, CartViewSet
from .views import ViewWishlist, WishlistAdd, WishlistRemove
from django.urls import path, include
from rest_framework import routers

app_name = "cart_shop"

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('cart/', ViewCart.as_view(), name='cart'),
    path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
    path('wishlist/add/<int:product_id>/', WishlistAdd.as_view(), name='wishlist_add'),
    path('wishlist/remove/<int:item_id>/', WishlistRemove.as_view(), name='wishlist_remove'),
    path('add/<int:product_id>/', ViewCartAdd.as_view(), name='add'),
    path('buy/<int:product_id>/', ViewCartBuy.as_view(), name='buy'),
    path('delete/<int:item_id>/', ViewCartDel.as_view(), name='delete'),
    path('api/', include(router.urls)),
]