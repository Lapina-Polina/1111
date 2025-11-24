from django.urls import path
from apps.common import views

app_name = 'store'

urlpatterns = [
    path('', views.ShopView.as_view(), name='shop'),
    path('product/<int:id>/', views.ProductSingleView.as_view(), name='product'),
]
