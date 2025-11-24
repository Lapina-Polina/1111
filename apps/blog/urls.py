from django.urls import path
from .views import BlogView, BlogSingleView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),
    path('post/<int:id>/', BlogSingleView.as_view(), name='single'),
]